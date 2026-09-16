---
description: Common Hydra documentation and lab mistakes involving scope, credentials, result interpretation, and defensive controls.
---
# Common mistakes

## Treating syntax as permission

A command that works is not automatically authorized. Keep the target, accounts, time window, and candidate data inside written scope.

## Using real credentials in examples

Public documentation should never contain a customer password, leaked password list, browser export, token, or production credential pair. Use synthetic data.

## Copying a real target into documentation

The original analysis note contained a real hostname. This public project intentionally replaces it with lab-only addresses. Do not reintroduce real third-party targets in issues, pull requests, screenshots, or examples.

## Misreading `F=`

`F=incorrect` is a response-matching rule, not proof of success when the text is absent. Validate possible matches independently.

## Ignoring account lockout

Repeated attempts can lock even a dedicated test account. Know the threshold and reset path before testing.

## Treating defensive controls as obstacles

CAPTCHA, MFA, CSRF/session requirements, throttling, and blocking are controls to document and validate—not controls this project teaches you to bypass.

## Reporting without context

Record the Hydra version, module, lab target, synthetic candidate source, control behavior, and validation status so another authorized tester can reproduce the finding safely.
