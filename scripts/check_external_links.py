from __future__ import annotations
import re, sys, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlsplit, urlunsplit
from urllib.request import Request, urlopen

MARKDOWN_LINK_RE=re.compile(r"!?\[[^\]]*\]\((https?://[^)\s]+)\)")
HTML_LINK_RE=re.compile(r"(?:href|src)=[\"'](https?://[^\"']+)[\"']",re.I)
WARNING_ONLY_HOSTS={"github.com","raw.githubusercontent.com","img.shields.io"}

def classify_http_status(status:int)->str:
    if 200<=status<400:return 'ok'
    if status in {404,410}:return 'error'
    return 'warning'

def is_warning_only_url(url:str)->bool:
    host=urlsplit(url).hostname or ''
    return host in WARNING_ONLY_HOSTS

def _ascii_url(url:str)->str:
    p=urlsplit(url)
    return urlunsplit((p.scheme,p.netloc,quote(p.path,safe="/%:@-._~!$&'()*+,;="),quote(p.query,safe="=&?/:;+,%@-._~!$'()*"),quote(p.fragment,safe="=&?/:;+,%@-._~!$'()*")))

def check_url(url:str,opener=urlopen,retries:int=1,timeout:int=8)->tuple[str,str]:
    req=Request(_ascii_url(url),headers={'User-Agent':'hydra-fa-reference-link-checker/1.0','Accept':'text/html,application/xhtml+xml,*/*;q=0.8','Range':'bytes=0-1023'},method='GET')
    last='unknown failure'
    for attempt in range(retries+1):
        try:
            with opener(req,timeout=timeout) as response: status=getattr(response,'status',200)
            return classify_http_status(status),f'HTTP {status}'
        except HTTPError as exc:
            state=classify_http_status(exc.code); last=f'HTTP {exc.code} {exc.reason}'
            if state=='error' or exc.code in {401,403}: return state,last
        except URLError as exc: last=str(exc.reason)
        except TimeoutError as exc: last=str(exc) or 'timeout'
        if attempt<retries: time.sleep(.25*(attempt+1))
    return 'warning',last

def collect_external_links(repo_root:Path)->set[str]:
    files=[]
    for d in (repo_root/'docs/fa',repo_root/'docs/en'):
        if d.exists(): files.extend(d.rglob('*.md'))
    files.extend(repo_root.glob('README*.md'))
    for extra in (repo_root/'SECURITY.md',repo_root/'site-root/index.html'):
        if extra.exists():files.append(extra)
    urls=set()
    for path in files:
        text=path.read_text(encoding='utf-8')
        urls.update(m.group(1).rstrip('.,') for m in MARKDOWN_LINK_RE.finditer(text))
        urls.update(m.group(1).rstrip('.,') for m in HTML_LINK_RE.finditer(text))
    return urls

def _check_one(url):
    state,msg=check_url(url); return url,state,msg

def main()->int:
    repo_root=Path(__file__).resolve().parents[1]; urls=sorted(collect_external_links(repo_root)); errors=[]; warnings=[]
    print(f'Checking {len(urls)} unique external link(s) with bounded concurrency...')
    with ThreadPoolExecutor(max_workers=min(8,max(1,len(urls)))) as pool: results=list(pool.map(_check_one,urls))
    for url,state,msg in results:
        warning_only=is_warning_only_url(url)
        if state=='error' and not warning_only: errors.append(f'{url}: {msg}')
        elif state in {'warning','error'}: warnings.append(f'{url}: {msg}' + (' (rate-limited host allowlist)' if warning_only else ''))
    if warnings:
        print('External link warnings:'); [print('  - '+x) for x in warnings]
    if errors:
        print('Deterministically broken external links:'); [print('  - '+x) for x in errors]; return 1
    print('External link check completed without non-allowlisted deterministic 404/410 failures.'); return 0
if __name__=='__main__': sys.exit(main())
