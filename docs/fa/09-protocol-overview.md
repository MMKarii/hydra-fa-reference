---
description: مرور مرجع‌محور خانواده پروتکل و Moduleهای Hydra بدون تبدیل شدن به مجموعه Attack Recipe.
---
# مرور پروتکل‌ها

Hydra بر مبنای Service Module کار می‌کند. فهرست دقیق Moduleها به Build وابسته است؛ بنابراین `hydra -h` و README upstream مرجع Version-specific هستند.

| خانواده | نمونه‌ها | تمرکز دفاعی |
|---|---|---|
| Remote access | SSH، RDP، VNC | Lockout، MFA، Source Control، Auth Log |
| File transfer | FTP | Password Policy، Exposure، Logging |
| Mail | SMTP، IMAP، POP3 | Throttling، Monitoring، Auth Control |
| Web | HTTP(S) GET/POST و Form | Session، Rate Limit، MFA، CAPTCHA، CSRF |
| Database | MySQL، PostgreSQL، MS-SQL | Network Exposure، Least Privilege، Auth Log |
| Directory/network | LDAP، SMB و دیگر موارد | Account Policy، Segmentation، Alerting |

این جدول Capability Map است، نه Recipe حمله. برای Help Module مجاز:

```bash
hydra -U ssh
```

کوچک‌ترین Procedure آزمایشگاهی که سؤال ارزیابی را جواب می‌دهد انتخاب کنید.
