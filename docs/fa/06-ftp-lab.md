---
description: آزمایشگاه کنترل‌شده Hydra برای ممیزی FTP با Credential مصنوعی و بررسی Log دفاعی.
---
# آزمایشگاه FTP

سند آموزشی اولیه یک مثال FTP دارد. نسخه عمومی از IP خصوصی و داده مصنوعی استفاده می‌کند:

```bash
hydra -L users.txt -P passwords.txt 192.168.56.20 ftp
```

FTP Service را مشخصاً برای تمرین آماده کنید و Candidate List را کوچک نگه دارید تا Lockout یا اختلال تصادفی رخ ندهد.

## چه چیزهایی باید بررسی شوند؟

- Hydra به FTP مورد انتظار متصل شود؛
- Server Log شکست‌های Login را ثبت کند؛
- Lockout/Throttling مطابق Policy عمل کند؛
- Credential ضعیف آزمایشگاهی فقط در صورت وجود در Candidate List شناسایی شود؛
- نتیجه قبل از گزارش به‌طور مستقل تأیید شود.

## برداشت دفاعی

Failureهای تکراری FTP می‌توانند Telemetry ارزشمند باشند. در محیط واقعی علاوه بر Password Policy و Monitoring، سرویس Legacy غیرضروری را حذف یا جایگزین کنید.
