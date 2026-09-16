---
description: آزمایشگاه کنترل‌شده Hydra برای ممیزی Password روی SSH با حساب مصنوعی و IP خصوصی.
---
# آزمایشگاه SSH

این فصل مثال SSH سند اولیه را به شبکه Lab محدود می‌کند.

## آماده‌سازی

یک SSH Server آزمایشگاهی در `192.168.56.10`، حساب مصنوعی مثل `labadmin` و فایل کوچک Password مخصوص تمرین داشته باشید. Owner سرویس باید Window تست و رفتار Lockout را بداند.

```bash
hydra -l labadmin -P passwords.txt 192.168.56.10 ssh
```

معنی پارامترها:

- `-l labadmin`: یک Login مصنوعی؛
- `-P passwords.txt`: Candidate List آزمایشگاهی؛
- `192.168.56.10`: Target خصوصی Lab؛
- `ssh`: انتخاب Module SSH.

## سمت دفاع را هم ببینید

در زمان اجرا Authentication Log، وضعیت Lockout، Alert Pipeline و کنترل‌های محدودکننده را مانیتور کنید. هدف فقط یافتن Credential ضعیف نیست؛ Detection و Response نیز باید اعتبارسنجی شوند.

## Stop Condition

اگر حساب تست برخلاف انتظار Lock شد، Host ناپایدار شد، Latency احراز هویت به‌طور محسوس بالا رفت یا فعالیت از Scope خارج شد، تست را متوقف کنید. این مشکل را با Optionهای Bypass/Evasion یا افزایش حجم حل نکنید.

## Validation

Credential گزارش‌شده را فقط با حساب تست و روش تأییدشده اعتبارسنجی کنید و پس از تمرین Password آزمایشگاهی را Reset کنید.
