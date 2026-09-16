# Hydra Reference v1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build `MMKarii/hydra-fa-reference` as a complete bilingual Persian/English Hydra reference with the same architecture, CI/QA, governance, accessibility, release discipline, and publishing model as the mature Nmap reference.

**Architecture:** Maintain mirrored `docs/fa/` and `docs/en/` trees, independent MkDocs Material configs, repository-local reading links, automated integrity checks, and a `gh-pages` deployment workflow. All runnable examples use synthetic lab targets only; no real target from the source documents is published.

**Tech Stack:** Markdown, MkDocs Material 9.x, GitHub Actions, Python 3 standard library QA scripts, HTML/CSS, SVG/WebP assets.

**Spec:** `docs/superpowers/specs/2026-09-16-hydra-reference-v1-design.md`

## Global Constraints

- Public examples use only controlled lab/synthetic targets such as `192.168.56.10`, `192.168.56.20`, and `192.168.56.101`.
- Do not include the real hostname from the uploaded source document, real credentials, customer data, or third-party login output.
- Do not publish stealth, lockout-bypass, CAPTCHA-bypass, MFA-bypass, or anti-detection guidance.
- Persian and English documentation filenames and navigation order must match.
- README reading links must work directly in GitHub before GitHub Pages is enabled.
- Original project-authored documentation is CC BY 4.0; upstream Hydra names/code retain upstream rights.

---

### Task 1: Build bilingual documentation content

**Files:** Create mirrored `docs/fa/*.md` and `docs/en/*.md` for 14 chapters plus learning path, cheat sheet, glossary, references, disclaimer, and index.

- [ ] Ground Persian content in the two source Word documents.
- [ ] Replace every real target with lab-only targets.
- [ ] Create English editions with matching structure and technical meaning.
- [ ] Add authoritative upstream/Kali references for technical expansion.
- [ ] Verify no forbidden real hostname appears anywhere in public content.

### Task 2: Add branding and site UX

**Files:** `docs/*/assets/brand-banner.webp`, `docs/*/assets/stylesheets/extra.css`, `assets/social-preview-v1.svg`, `site-root/index.html`, `overrides/main.html`.

- [ ] Convert the supplied 2048px Hydra banner to high-quality WebP without visible downscaling.
- [ ] Add responsive RTL/LTR styling, focus visibility, reduced motion, mobile-safe code/tables, and Hydra dark/cyan/red accents.
- [ ] Add bilingual landing and Open Graph/Twitter metadata.

### Task 3: Add repository entry points and governance

**Files:** `README.md`, `README.fa.md`, `README.en.md`, `LICENSE`, `DISCLAIMER.md`, `CONTRIBUTING.md`, `SECURITY.md`, `.github/*` community files.

- [ ] Make GitHub-local Persian/English reading links primary.
- [ ] Add CC BY 4.0 with upstream-Hydra rights distinction.
- [ ] Add safety/privacy requirements to Issue and PR templates.

### Task 4: Add MkDocs configs and QA tooling with tests

**Files:** `mkdocs.fa.yml`, `mkdocs.en.yml`, `requirements.txt`, `scripts/check_*.py`, `scripts/test_*.py`.

- [ ] Test language parity, local links/anchors, translation drift, external-link classification/encoding, and built HTML metadata/alt text.
- [ ] Run `python -m unittest discover -s scripts -p 'test_*.py'` and `python scripts/check_docs.py`.
- [ ] Strict-build both language editions.

### Task 5: Add CI/CD and versioned publishing

**Files:** `.github/workflows/docs.yml`.

- [ ] Run QA and strict builds on PR/main.
- [ ] Publish current, `/latest/`, and `/v1.0/` outputs.
- [ ] Render the social preview and deploy successful main builds to `gh-pages`.

### Task 6: Release documentation

**Files:** `CHANGELOG.md`, `.github/release-notes/v1.0.0.md`.

- [ ] Record bilingual docs, CI/QA, accessibility, branding, governance, and lab-only safety scope.
- [ ] After green merge/main CI, publish `v1.0.0 — Bilingual Edition`.

### Task 7: Pull request and final verification

- [ ] Commit implementation on `hydra-docs-v1` and open a PR to `main`.
- [ ] Confirm CI succeeds and merge only with the expected head SHA.
- [ ] Confirm post-merge CI and `gh-pages` deployment.
- [ ] Verify Pages/About/branch protection state and report unsupported administrative settings accurately.
