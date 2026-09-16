# Hydra Reference v1 — Design Specification

## Goal

Build `MMKarii/hydra-fa-reference` as a professional bilingual Persian/English Hydra documentation project with the same repository architecture, quality gates, publishing discipline, visual polish, governance, and maintenance model used for `MMKarii/nmap-fa-reference`.

The project is an educational and defensive-security reference for authorized password auditing and authentication testing. It must not publish real targets, real credentials, or instructions whose purpose is unauthorized access.

## Source inputs

The first edition is grounded in the two user-provided Word documents and the supplied Hydra banner image.

Source-derived topics include:

- Hydra as an authentication testing / password auditing tool.
- Kali Linux installation and `hydra -h` verification.
- Username and password input files.
- General command structure.
- Authorized SSH and FTP lab examples.
- HTTP/HTTPS form testing structure using placeholders such as `^USER^` and `^PASS^`.
- Failure-string logic such as `F=incorrect` and the risk of false positives.
- Practical limitations including CSRF tokens, CAPTCHA, rate limiting, IP blocking, and greylisting.
- Recommended legal lab environments such as DVWA, OWASP Juice Shop, and Metasploitable.
- Explicit legal/ethical framing for personal systems, training labs, and written authorization.

The real hostname present in one source document must never appear in the public repository. It must be replaced by lab-only examples such as `192.168.56.101` or non-routable documentation placeholders.

When the project expands beyond the supplied source material, added technical facts must be verified against official Hydra/Kali documentation or another authoritative primary source and must be clearly written as project-authored documentation rather than silently attributed to the uploaded Word files.

## Safety and scope rules

These rules apply to every README, chapter, example, issue template, release note, and generated site page:

1. Examples are limited to systems the reader owns, controlled lab environments, or explicitly authorized assessments.
2. No public documentation may contain a real organization domain, real customer host, private credential, API token, password dump, or real scan/login output tied to a third party.
3. Default examples use lab targets such as `192.168.56.10`, `192.168.56.20`, and `192.168.56.101`.
4. The project may explain how Hydra interprets login failure/success conditions, but it must not provide stealth, evasion, lockout-bypass, CAPTCHA-bypass, MFA-bypass, or anti-detection guidance.
5. The project must not optimize high-volume credential attacks against real services. Rate-related content is framed around minimizing lab impact, understanding defensive controls, and avoiding accidental lockouts.
6. Defensive material should explain CAPTCHA, CSRF, MFA, rate limiting, account lockout, IP reputation/blocking, monitoring, and alerting as protections.
7. The repository disclaimer must distinguish repository documentation issues from upstream Hydra vulnerabilities.

## Repository architecture

The repository mirrors the mature Nmap project architecture:

```text
.
├── .github/
│   ├── CODEOWNERS
│   ├── ISSUE_TEMPLATE/
│   ├── pull_request_template.md
│   ├── repository-metadata.md
│   ├── branch-protection.md
│   └── workflows/docs.yml
├── assets/
│   └── social-preview-v1.svg
├── docs/
│   ├── fa/
│   │   ├── index.md
│   │   ├── 01-introduction.md
│   │   ├── 02-installation.md
│   │   ├── 03-syntax.md
│   │   ├── 04-credential-inputs.md
│   │   ├── 05-ssh-lab.md
│   │   ├── 06-ftp-lab.md
│   │   ├── 07-http-form-basics.md
│   │   ├── 08-login-result-detection.md
│   │   ├── 09-protocol-overview.md
│   │   ├── 10-safe-lab-operation.md
│   │   ├── 11-output-reporting.md
│   │   ├── 12-defensive-controls.md
│   │   ├── 13-troubleshooting.md
│   │   ├── 14-common-mistakes.md
│   │   ├── learning-path.md
│   │   ├── cheatsheet.md
│   │   ├── glossary.md
│   │   ├── references.md
│   │   ├── disclaimer.md
│   │   └── assets/
│   │       ├── brand-banner.webp
│   │       └── stylesheets/extra.css
│   └── en/
│       └── exact mirrored filenames and structure
├── overrides/main.html
├── scripts/
│   ├── check_docs.py
│   ├── check_external_links.py
│   ├── check_built_site.py
│   └── test_*.py
├── site-root/index.html
├── mkdocs.fa.yml
├── mkdocs.en.yml
├── requirements.txt
├── README.md
├── README.fa.md
├── README.en.md
├── CONTRIBUTING.md
├── SECURITY.md
├── DISCLAIMER.md
├── CHANGELOG.md
└── LICENSE
```

## Documentation structure

Persian and English editions must have identical filenames and navigation order.

### 01 — Introduction / معرفی

Explain what Hydra is, the password-auditing/authentication-testing model, authorized-use boundaries, supported-service concept, and why controlled labs are required.

### 02 — Installation / نصب

Cover Kali Linux availability, package installation, version/help verification, and basic troubleshooting of installation only.

### 03 — Syntax / ساختار دستور

Explain the general form `hydra [options] target service`, single versus list-based username/password inputs, and how target/service/module selection fits together.

### 04 — Credential inputs / ورودی‌های نام کاربری و رمز عبور

Explain controlled lab wordlists, file formatting, sample synthetic usernames/passwords, hygiene, and avoiding real credential collections.

### 05 — SSH lab

Use only a controlled lab target. Explain the source-provided SSH example at a conceptual and lab-safe level, parameters, expected lab behavior, and defensive observations such as authentication logs and lockout risk.

### 06 — FTP lab

Use only a controlled lab target. Explain the source-provided FTP example, parameters, expected lab behavior, and server-side logging/defensive considerations.

### 07 — HTTP/HTTPS form basics

Explain the form module structure using lab-only targets, request path, form fields, `^USER^`/`^PASS^`, and failure-condition syntax. Do not reproduce or reference the real hostname from the source document.

### 08 — Login result detection

Explain `F=` failure matching, the meaning of a missing failure string, false-positive risk, redirects/session behavior at a high level, and why validation in a controlled lab is required.

### 09 — Protocol overview

Provide a reference-oriented overview of common protocol families supported by Hydra, aligned with authoritative documentation. This is a capability/reference page, not a collection of attack recipes.

### 10 — Safe lab operation

Cover scope definition, minimizing request volume, avoiding accidental lockout, test-account preparation, logging, evidence handling, and stopping conditions. Do not include evasion or anti-detection techniques.

### 11 — Output and reporting

Explain how to record reproducible lab results, distinguish confirmed findings from possible/false-positive results, and document defensive remediation.

### 12 — Defensive controls

Explain the protections already identified in the source documents: CAPTCHA, CSRF, rate limiting, IP blocking/greylisting, plus MFA, lockout, monitoring, and alerting where supported by authoritative sources.

### 13 — Troubleshooting

Cover common lab failures: wrong form path, wrong field names, wrong failure string, redirects, CSRF-protected forms, network reachability, module mismatch, and false positives. Troubleshooting remains lab-scoped.

### 14 — Common mistakes

Summarize unsafe scope assumptions, using real credentials/targets, incorrect result interpretation, ignoring rate limits/lockouts, poor evidence handling, and failure to verify success independently.

## Learning path, cheat sheet, glossary, references, disclaimer

Both languages include mirrored auxiliary pages:

- `learning-path.md`: beginner → intermediate → defensive validation path.
- `cheatsheet.md`: compact lab-only command/reference patterns, with no real targets.
- `glossary.md`: Persian/English terminology aliases for Hydra, credential auditing, authentication, failure condition, CSRF, CAPTCHA, rate limiting, lockout, false positive, and related terms.
- `references.md`: official/authoritative sources used for technical verification.
- `disclaimer.md`: legal/ethical use, authorization, no warranty, and upstream-project distinction.

## README behavior

The root README follows the Nmap project style:

- Hydra banner at full width.
- Build, language, reference, and CC BY 4.0 badges.
- Short bilingual project description.
- Two primary cards/links for Persian and English.
- Primary reading links must work directly inside GitHub (`docs/fa/index.md` and `docs/en/index.md`) even if GitHub Pages has not yet been enabled.
- Online Pages links may be shown only after Pages is verified as active.
- Explicit authorized-use warning above practical examples.

Dedicated `README.fa.md` and `README.en.md` provide language-specific quick access, chapter lists, learning path, cheat sheet, references, and license links.

## Branding and visual design

The supplied Hydra image is the canonical brand source.

- Preserve its visual identity.
- Convert an optimized high-quality WebP version for README and both documentation editions.
- Do not downscale to a visibly soft/low-quality asset.
- Create a separate 1280×640 social-preview asset with reduced text density for Open Graph/social sharing.
- Persian pages use RTL styling; English pages use LTR styling.
- Both editions use consistent dark/cyan/red Hydra visual accents while preserving readable contrast.
- Include keyboard focus states, mobile layouts, reduced-motion support, scrollable code/table blocks, and safe mixed RTL/LTR rendering.

## MkDocs and site publishing

Use Material for MkDocs with two independent configs:

- `mkdocs.fa.yml`: Persian, RTL, Persian/English search tokenization.
- `mkdocs.en.yml`: English, LTR.

Both configs include:

- search suggestions/highlighting;
- bilingual alternate-language links;
- shared theme override for canonical, description, Open Graph, and Twitter Card metadata;
- strict builds;
- glossary navigation;
- custom CSS.

The root `site-root/index.html` is a bilingual language selector.

Publishing layout after `v1.0.0` exists:

- `/fa/`
- `/en/`
- `/latest/fa/`
- `/latest/en/`
- `/v1.0/fa/`
- `/v1.0/en/`

The workflow deploys the built `site/` tree to `gh-pages`. README links remain GitHub-local until GitHub reports Pages as enabled.

## QA and CI

The `docs` workflow runs on pull requests to `main`, pushes to `main`, and manual dispatch.

Required checks:

1. Python unit tests for documentation tooling.
2. Persian/English file-structure parity.
3. Local Markdown link validation.
4. Markdown anchor validation.
5. Translation-drift reporting.
6. External-link checking with deterministic 404/410 failures and warning-only transient/blocked responses.
7. Strict Persian MkDocs build.
8. Strict English MkDocs build.
9. Built-site checks for HTML language, title, description, viewport, and project-controlled image alt text.
10. Verification of root, language, latest, versioned, banner, glossary, and social-preview outputs.
11. Deploy only when the `main` push build is successful.

CI must never require paid services or repository secrets beyond the standard GitHub Actions token.

## Governance

Add the same governance model as the Nmap project:

- `CODEOWNERS` owned by `@MMKarii`.
- Issue templates for technical correction, translation issue, broken link, and feature request.
- PR template requiring language parity, references, safe examples, and CI checks.
- `SECURITY.md` for private handling of repository security issues and explicit separation from upstream Hydra vulnerabilities.
- `.github/branch-protection.md` documenting recommended `main` protection when the connected API cannot configure it directly.
- `.github/repository-metadata.md` with desired description, website, and topics.

## License

Original project-authored documentation is released under Creative Commons Attribution 4.0 International (CC BY 4.0), matching the Nmap reference project.

Third-party project names, trademarks, upstream documentation, and linked content retain their own rights.

## Release model

The first complete production milestone is `v1.0.0 — Bilingual Edition`.

Before release:

- both language builds pass with `--strict`;
- all QA checks pass;
- banner and social preview are verified;
- no real targets/credentials are present;
- `CHANGELOG.md` contains the v1.0.0 entry;
- release notes summarize bilingual docs, source grounding, governance, CI, accessibility, and lab-only safety boundaries.

The existing release/tag must never be rewritten after publication. Later versions append new changelog entries and snapshots.

## Git workflow

Because the repository begins empty:

1. This design specification initializes `main`.
2. Implementation occurs on a dedicated `hydra-docs-v1` branch created from `main`.
3. The implementation is reviewed through a pull request.
4. Merge happens only after CI is green.
5. `v1.0.0` is tagged/released only after the merged `main` build succeeds.
6. GitHub Pages and repository About metadata are verified after release; unsupported administrative settings are documented rather than falsely reported as active.

## Definition of done

The project is complete when all of the following are true:

- Repository has professional bilingual Persian/English documentation with mirrored structure.
- All 14 chapters and auxiliary pages exist in both languages.
- The uploaded source material has been incorporated without the real target hostname.
- All examples use lab/synthetic targets only.
- Banner is sharp and correctly displayed on GitHub.
- README links work even before GitHub Pages is enabled.
- CC BY 4.0, contribution, security, disclaimer, and governance files exist.
- CI validates structure, links, anchors, translation freshness, external references, both strict builds, and built-site metadata/accessibility.
- PR is merged only after green CI.
- `CHANGELOG.md` and GitHub Release `v1.0.0` exist.
- `gh-pages` deployment succeeds.
- Any GitHub administrative setting that could not be applied through the connector is explicitly reported as remaining work rather than claimed complete.
