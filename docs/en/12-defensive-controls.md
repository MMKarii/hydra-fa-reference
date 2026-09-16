---
description: Defensive controls relevant to Hydra-style authentication testing: MFA, rate limiting, lockout, CAPTCHA, CSRF, logging, and alerting.
---
# Defensive controls

The supplied notes explicitly identify CAPTCHA, CSRF tokens, rate limiting, and IP blocking/greylisting as practical constraints. Those controls are part of a broader authentication defense.

## Rate limiting and lockout

Rate limiting slows repeated attempts. Account lockout can stop repeated failures but must be designed carefully to avoid making denial-of-service against user accounts easy. Test both the security effect and the operational recovery process.

## MFA

Multi-factor authentication reduces the value of a compromised password by requiring another factor. This project does not document MFA-bypass techniques; an MFA-protected flow is treated as a control to validate from the defensive side.

## CAPTCHA and anti-automation

CAPTCHA and similar challenges can disrupt automated login attempts. In an authorized assessment, document the control and its coverage rather than attempting to defeat it with this reference.

## CSRF and session protections

CSRF tokens are primarily intended to prevent cross-site request forgery, but dynamic per-session values can also make simplistic replay/automation fail. A Hydra form definition that cannot maintain required application state is not evidence that the authentication control is weak or strong by itself.

## Monitoring and alerting

Correlate repeated failures, source addresses, account names, time windows, and successful logins after failure bursts. Good detection should support investigation without exposing full passwords or sensitive session data in logs.
