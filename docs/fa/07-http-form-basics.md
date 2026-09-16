---
description: مبانی ماژول فرم HTTP/HTTPS در Hydra با Target آزمایشگاهی و Failure Matching ساده.
---
# مبانی فرم‌های HTTP/HTTPS

اسناد اولیه بیشترین تمرکز را روی Form Login دارند. upstream Hydra Moduleهایی مانند `http-post-form` و `https-post-form` را برای فرم‌های ساده Username/Password مستند کرده است.

مثال Lab مطابق منبع اولیه:

```bash
hydra -L users.txt -P passwords.txt 192.168.56.101 https-post-form \
  "/login.php:user=^USER^&pass=^PASS^:F=incorrect"
```

## خواندن Module String

این رشته سه بخش اصلی دارد:

1. `/login.php` — Path فرم آزمایشگاهی؛
2. `user=^USER^&pass=^PASS^` — Fieldهایی که Hydra Candidateها را جایگزین می‌کند؛
3. `F=incorrect` — شرط شکست؛ اگر پاسخ شامل `incorrect` باشد، تلاش Failed محسوب می‌شود.

Source Module upstream شرط `S=` را نیز برای Success مستند می‌کند. این مرجع برای هم‌راستایی با سند اولیه روی Failure Matching ساده تمرکز دارد.

## Form Shape را از Lab بگیرید

Request Method، Action، Field Name و Failure Indicator را فقط از Application خودتان یا Training Target استخراج کنید. Request یک Login واقعی شخص ثالث را وارد Documentation نکنید.

## چرا فرم ساده مناسب‌تر است؟

Application مدرن ممکن است CSRF Token، CAPTCHA، MFA، JavaScript پویا، Session Flow پیچیده و Rate Control داشته باشد. این کنترل‌ها نشانه‌ای برای توقف یا انتخاب Lab مناسب‌تر هستند، نه چیزی که این مرجع روش Bypass آن را آموزش دهد.
