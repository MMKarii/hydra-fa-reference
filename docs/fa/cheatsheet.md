---
description: مرجع سریع و آزمایشگاهی Hydra برای Syntax، Credential File، SSH، FTP، HTTP Form و Validation.
---
# Hydra Cheat Sheet

مرجع سریع برای Lab کنترل‌شده. همه Targetها و Credentialها مصنوعی هستند.

## بررسی نصب

```bash
hydra -h
```

## Credential Inputs

```bash
hydra -l labadmin -P passwords.txt 192.168.56.10 ssh
```

```bash
hydra -L users.txt -P passwords.txt 192.168.56.20 ftp
```

## فرم ساده HTTPS در Lab

```bash
hydra -L users.txt -P passwords.txt 192.168.56.101 https-post-form \
  "/login.php:user=^USER^&pass=^PASS^:F=incorrect"
```

`^USER^` و `^PASS^` Placeholder هستند. `F=incorrect` یعنی پاسخ شامل `incorrect` به‌عنوان Failure طبقه‌بندی شود.

## Module Help

```bash
hydra -U ssh
hydra -U http-post-form
```

## Rule اعتبارسنجی

Credential Match گزارش‌شده توسط Tool تا زمانی که با حساب Lab و Evidence سمت Server تأیید نشود، **Confirmed** نیست.

## Stop به‌جای Bypass

اگر MFA، CAPTCHA، Lockout، Rate Limit یا CSRF/Session پویا مانع Procedure ساده شد، Control را مستند یا از Training Target مناسب استفاده کنید. این Cheat Sheet راه Bypass ارائه نمی‌دهد.
