# Recommended `main` branch protection

The connected GitHub integration may not expose repository-administration writes. Apply these settings when supported and do not report them as active until GitHub confirms them.

- Require a pull request before merging.
- Require status checks to pass before merging.
- Required check: `build-and-deploy` from `.github/workflows/docs.yml`.
- Require branches to be up to date before merging when practical.
- Require at least one approving review for non-owner/community contributions.
- Require conversation resolution before merging.
- Block force pushes.
- Block branch deletion.
- Do not allow ordinary contributors to bypass the rules.
