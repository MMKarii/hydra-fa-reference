<p align="center">
  <img src="docs/fa/assets/brand-banner.webp" alt="Hydra Persian Reference" width="100%">
</p>

<p align="center"><a href="README.md">انتخاب زبان</a> · <a href="README.en.md">English</a></p>

<h1 align="center">مرجع جامع فارسی Hydra</h1>

<p align="center">مستند فصل‌بندی‌شده برای یادگیری Hydra، ممیزی مجاز احراز هویت و تحلیل کنترل‌های دفاعی با تجربه کاربری RTL.</p>

<p align="center">
  <a href="docs/fa/index.md">مطالعه نسخه فارسی</a> ·
  <a href="docs/fa/learning-path.md">مسیر یادگیری</a> ·
  <a href="docs/fa/cheatsheet.md">Cheat Sheet</a> ·
  <a href="docs/fa/references.md">منابع فنی</a> ·
  <a href="LICENSE">مجوز</a>
</p>

> [!IMPORTANT]
> Hydra را فقط روی سیستم شخصی، محیط آزمایشگاهی یا سامانه‌ای اجرا کنید که برای آزمون آن مجوز صریح دارید. هیچ مثال این پروژه برای هدف واقعی شخص ثالث نوشته نشده است.

## درباره پروژه

این ریپو نسخه فارسی و انگلیسی یک مرجع حرفه‌ای Hydra است. موضوعات پایه از دو سند آموزشی ارائه‌شده استخراج شده‌اند: نصب، فایل‌های نام کاربری/رمز عبور، SSH و FTP آزمایشگاهی، فرم HTTP/HTTPS، منطق `F=` و محدودیت‌هایی مانند CSRF، CAPTCHA و Rate Limiting. جزئیات تکمیلی با منابع رسمی Hydra و Kali تطبیق داده می‌شوند.

## فصل‌ها

| فصل | موضوع |
|---:|---|
| 1 | [معرفی بنیادین Hydra](docs/fa/01-introduction.md) |
| 2 | [نصب و بررسی](docs/fa/02-installation.md) |
| 3 | [Syntax و ساختار دستور](docs/fa/03-syntax.md) |
| 4 | [ورودی‌های نام کاربری و رمز عبور](docs/fa/04-credential-inputs.md) |
| 5 | [آزمایشگاه SSH](docs/fa/05-ssh-lab.md) |
| 6 | [آزمایشگاه FTP](docs/fa/06-ftp-lab.md) |
| 7 | [مبانی فرم‌های HTTP/HTTPS](docs/fa/07-http-form-basics.md) |
| 8 | [تشخیص موفقیت و شکست ورود](docs/fa/08-login-result-detection.md) |
| 9 | [مرور پروتکل‌ها](docs/fa/09-protocol-overview.md) |
| 10 | [اجرای ایمن در آزمایشگاه](docs/fa/10-safe-lab-operation.md) |
| 11 | [خروجی و گزارش‌دهی](docs/fa/11-output-reporting.md) |
| 12 | [کنترل‌های دفاعی](docs/fa/12-defensive-controls.md) |
| 13 | [عیب‌یابی](docs/fa/13-troubleshooting.md) |
| 14 | [اشتباهات رایج](docs/fa/14-common-mistakes.md) |

## شروع سریع آزمایشگاهی

```bash
hydra -l labadmin -P passwords.txt 192.168.56.10 ssh
```

از حساب و Wordlist مصنوعی استفاده کنید و پیش از آزمون، Scope، توقف اضطراری و سیاست Lockout را مشخص کنید.

## مجوز

محتوای اصلی این پروژه تحت CC BY 4.0 منتشر می‌شود. Hydra اصلی پروژه‌ای مستقل با حقوق و مجوز upstream خود است.
