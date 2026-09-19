import io, unittest
from urllib.error import HTTPError, URLError
from scripts.check_external_links import _ascii_url, check_url, classify_http_status, is_warning_only_url
class _Response:
    def __init__(self,status=200): self.status=status
    def __enter__(self): return self
    def __exit__(self,*args): return False
class ExternalLinkTests(unittest.TestCase):
    def test_status_classification(self):
        for status,state in [(200,'ok'),(301,'ok'),(403,'warning'),(429,'warning'),(404,'error'),(410,'error'),(500,'warning')]: self.assertEqual(classify_http_status(status),state)
    def test_project_pages_urls_are_not_allowlisted(self):
        self.assertFalse(is_warning_only_url('https://mmkarii.github.io/hydra-fa-reference/'))
        self.assertTrue(is_warning_only_url('https://github.com/MMKarii/hydra-fa-reference'))
    def test_unicode_url_is_ascii_encoded(self): _ascii_url('https://example.test/راهنما?q=هیدرا').encode('ascii')
    def test_success(self): self.assertEqual(check_url('https://example.test/',opener=lambda *_a,**_k:_Response(200))[0],'ok')
    def test_404_fails(self):
        def opener(request,timeout=0): raise HTTPError(request.full_url,404,'Not Found',{},io.BytesIO())
        self.assertEqual(check_url('https://example.test/missing',opener=opener,retries=0)[0],'error')
    def test_transient_warns(self):
        def opener(_request,timeout=0): raise URLError('temporary DNS failure')
        self.assertEqual(check_url('https://example.test/transient',opener=opener,retries=0)[0],'warning')
if __name__=='__main__': unittest.main()
