---
description: Record and report Hydra lab results with validation status, evidence hygiene, and remediation context.
---
# Output and reporting

Hydra output is test evidence, not the final conclusion. A useful report separates what the tool said from what was independently verified.

## Record the procedure

Capture:

- Hydra version/help header;
- test date and approved scope;
- lab target identifier;
- service/module;
- synthetic account and candidate-file identifiers;
- relevant defensive controls;
- stop conditions and whether they were triggered.

## Classify results

Use clear states such as:

- **confirmed** — authentication success was safely validated with the test account;
- **possible / tool-reported** — Hydra indicated a possible match but confirmation is pending;
- **false positive** — independent validation showed the report was incorrect;
- **control effective** — the test was blocked/throttled/locked out as designed.

## Remediation context

A weak test credential should lead to a recommendation tied to the system: stronger credential policy, MFA, lockout/rate limiting, service exposure reduction, logging, or alerting. Do not include the real password in a public issue or documentation update.
