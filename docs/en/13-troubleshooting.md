---
description: Troubleshoot Hydra lab tests without turning failures into bypass or evasion guidance.
---
# Troubleshooting

Troubleshooting should answer "why is my controlled lab procedure not representing the application correctly?" rather than "how do I bypass the defense?"

## SSH/FTP problems

Check basic reachability, service availability, the selected module, the synthetic account, and whether the service permits the tested authentication method. Review server logs for the authoritative reason.

## Web-form problems

Common lab mistakes include:

- wrong form path;
- wrong field names;
- wrong HTTP/HTTPS module;
- incorrect `F=` text;
- redirects that make every response look similar;
- CSRF/session requirements;
- a form rendered or submitted primarily by client-side JavaScript.

Use a known-invalid test login to establish the expected failure response. If the form requires dynamic state Hydra is not modeling, stop and document that limitation.

## False positives

If Hydra reports a match, verify it independently with the lab account. Never treat absence of the failure string as sufficient proof by itself.

## Avoid escalation-by-troubleshooting

Do not solve a failed test by adding evasion, anti-detection, CAPTCHA bypass, MFA bypass, or lockout bypass. Those are outside this project's scope.
