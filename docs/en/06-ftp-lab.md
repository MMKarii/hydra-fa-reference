---
description: Controlled Hydra FTP authentication-auditing lab with synthetic accounts and logging review.
---
# FTP lab

The supplied training notes include an FTP example. This version keeps the same learning objective while using a private lab address and synthetic data.

```bash
hydra -L users.txt -P passwords.txt 192.168.56.20 ftp
```

Prepare the FTP service specifically for the exercise. Keep the candidate lists small enough to avoid accidental denial of service or account lockout.

## What to verify

- Hydra reaches the expected FTP service and module.
- The server records failed authentication events as expected.
- Account lockout or throttling behavior matches policy.
- A deliberately weak lab credential is identified only if it exists in the synthetic candidate list.
- The result is independently confirmed before it is reported.

## Defensive interpretation

Repeated FTP login failures can be useful telemetry. A strong environment should combine secure credential policy with logging, alerting, rate controls where appropriate, and service reduction: disable or replace legacy FTP when it is not required.
