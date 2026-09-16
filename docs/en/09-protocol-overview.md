---
description: Reference overview of common Hydra protocol/module families without turning the page into attack recipes.
---
# Protocol overview

Hydra is designed around service modules. The exact list depends on the build, so `hydra -h` and the upstream README are the version-specific references.

Common families include:

| Family | Examples | Defensive review focus |
|---|---|---|
| Remote shell/access | SSH, RDP, VNC | lockout, MFA, source controls, authentication logs |
| File transfer | FTP | password policy, legacy-service exposure, logging |
| Mail | SMTP, IMAP, POP3 | authentication controls, throttling, monitoring |
| Web | HTTP(S) GET/POST and form modules | session handling, rate limiting, MFA, CAPTCHA, CSRF |
| Databases | MySQL, PostgreSQL, MS-SQL | network exposure, least privilege, authentication logs |
| Directory/network services | LDAP, SMB and others | account policy, segmentation, lockout, alerting |

This table is a capability map, not a collection of recipes. For a module-specific authorized test, read its installed help:

```bash
hydra -U ssh
```

Use the smallest lab procedure that answers the assessment question. Do not assume every available module is appropriate to run.
