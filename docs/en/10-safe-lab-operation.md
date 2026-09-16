---
description: Plan Hydra authentication tests safely with scope, test accounts, request restraint, and stop conditions.
---
# Safe lab operation

Authentication testing can create account lockouts and noisy telemetry even in a lab. Treat the procedure like a controlled change.

## Pre-test checklist

- confirm written scope and target ownership;
- use dedicated test accounts whenever possible;
- use synthetic candidate files;
- document lockout thresholds and reset steps;
- notify the system owner or lab operator;
- define a stop condition before execution;
- collect server-side logs for validation.

## Keep request volume intentional

Do not increase concurrency or retry behavior simply because a test is slow. The objective is to verify a security property—not to maximize attempts. Start with the smallest candidate set that proves the control works.

## Production caution

A production authentication test needs stricter approval because it can affect real users, trigger incident response, or lock privileged accounts. This project does not provide operational tuning for high-volume production credential attempts.

## Evidence hygiene

Store only the minimum evidence needed. Redact unrelated usernames, session identifiers, tokens, IP inventories, and other sensitive data before attaching logs to issues or reports.
