---
description: Lab-only Hydra quick reference for syntax, credential files, SSH, FTP, HTTP forms, and validation.
---
# Hydra Cheat Sheet

Quick reference for controlled labs. All targets and credentials are synthetic.

## Verify installation

```bash
hydra -h
```

## Credential inputs

```bash
hydra -l labadmin -P passwords.txt 192.168.56.10 ssh
```

```bash
hydra -L users.txt -P passwords.txt 192.168.56.20 ftp
```

## Simple HTTPS form lab

```bash
hydra -L users.txt -P passwords.txt 192.168.56.101 https-post-form \
  "/login.php:user=^USER^&pass=^PASS^:F=incorrect"
```

`^USER^` and `^PASS^` are substitution placeholders. `F=incorrect` means responses containing `incorrect` are classified as failures.

## Module help

```bash
hydra -U ssh
hydra -U http-post-form
```

## Validation rule

A tool-reported possible credential match is **not confirmed** until it is safely validated with the designated lab account and server-side evidence.

## Stop rather than bypass

If MFA, CAPTCHA, lockout, rate limiting, or dynamic CSRF/session handling prevents the simple lab procedure from working, document the control or move to a purpose-built training target. This cheat sheet does not provide bypass guidance.
