---
description: Hydra HTTP and HTTPS form module basics using lab-only targets and simple failure matching.
---
# HTTP/HTTPS form basics

The supplied notes focus heavily on form testing. Upstream Hydra documents form modules such as `http-post-form` and `https-post-form` for simple username/password forms.

A lab-only example based on the source material is:

```bash
hydra -L users.txt -P passwords.txt 192.168.56.101 https-post-form \
  "/login.php:user=^USER^&pass=^PASS^:F=incorrect"
```

## Read the module string

The module argument has colon-separated parts:

1. `/login.php` — the lab form path;
2. `user=^USER^&pass=^PASS^` — form fields where Hydra substitutes candidate values;
3. `F=incorrect` — a failure condition: if the response contains that text, the attempt is treated as failed.

The upstream form-module source also documents an `S=` success condition. This reference deliberately keeps examples to the simple failure-matching case supplied by the training notes.

## Collect the form shape safely

Before automating a lab form, inspect the HTML/request in your own application or training platform. Confirm the request method, action path, field names, and a stable failure indicator. Do not reuse request details from a real third-party login page.

## Why simple forms are easiest

Modern applications often add CSRF tokens, CAPTCHA, MFA, dynamic JavaScript, complex session flows, and rate controls. Those mechanisms can make a simple Hydra form definition unsuitable. This project treats such controls as reasons to stop or choose a purpose-built lab—not as obstacles to bypass.
