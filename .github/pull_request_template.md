## Summary

Describe what changes and why.

## Documentation scope

- [ ] Persian and English files remain structurally aligned when content changes affect both editions.
- [ ] Terminology is consistent with the glossary and upstream Hydra terminology.
- [ ] Examples remain limited to labs or explicitly authorized security assessments.
- [ ] No credentials, secrets, customer identifiers, real target hostnames, private inventories, or sensitive authentication data are included.
- [ ] No MFA/CAPTCHA/lockout bypass or anti-detection guidance is introduced.

## Quality checks

- [ ] Local links and anchors resolve.
- [ ] External references were checked or intentionally documented.
- [ ] `python -m unittest discover -s scripts -p 'test_*.py'` passes.
- [ ] `python scripts/check_docs.py` passes.
- [ ] Persian and English MkDocs builds pass with `--strict`.
- [ ] Mobile/RTL/LTR rendering was considered for visual changes.

## Release impact

- [ ] No release note needed.
- [ ] Changelog/release notes are updated when user-visible publishing behavior changes.
