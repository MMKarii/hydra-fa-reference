---
description: Introduction to Hydra as an authorized authentication testing and password-auditing tool.
---
# Hydra fundamentals

<div class="chapter-meta">Goal: understand what Hydra is, what this reference covers, and the authorization boundary before running any command.</div>

Hydra is a command-line authentication-testing tool that can try supplied login and password candidates against many network services and simple web login forms. The supplied training material frames it as an educational tool for understanding authentication security, and the upstream project describes it as proof-of-concept software for researchers and security consultants.

This reference keeps that same boundary: **personal systems, controlled labs, or explicitly authorized assessments only**. It does not provide guidance for hiding activity, bypassing MFA/CAPTCHA/lockout controls, or targeting real third parties.

## What Hydra evaluates

A typical lab exercise has four parts:

1. a known in-scope target such as `192.168.56.10`;
2. a service/module such as `ssh`, `ftp`, or `http-post-form`;
3. a small synthetic set of usernames/passwords;
4. a rule for interpreting whether authentication failed or might have succeeded.

Hydra automates repeated authentication attempts. That makes it useful for demonstrating weak password policy, validating lockout/rate-limiting behavior, and testing whether a defensive control detects repeated failures. It also means careless use can lock accounts or generate significant authentication traffic.

## What this project adds

The two maintainer-supplied Persian notes cover installation on Kali, credential files, SSH and FTP lab examples, HTTP/HTTPS form syntax, `F=` failure matching, false positives, CSRF/CAPTCHA/rate-limit constraints, and authorized-use guidance. This project reorganizes those topics into mirrored Persian and English documentation and adds maintenance, reporting, accessibility, and QA material.

For exact option/module behavior, always check the installed `hydra -h`, `hydra -U <module>`, and the upstream project documentation because behavior can change by version and build options.

## Before continuing

Define the approved target, testing window, test account, synthetic candidate list, lockout policy, and an immediate stop condition. If any of those are unknown, do not run the authentication test yet.
