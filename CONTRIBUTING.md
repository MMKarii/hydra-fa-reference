# مشارکت در پروژه

این پروژه یک مرجع فنی دو زبانه برای Hydra است. تغییرات باید از نظر دقت فنی، ایمنی مثال‌ها و هماهنگی نسخه فارسی/انگلیسی قابل دفاع باشند.

## منابع

برای ادعاهای فنی فراتر از اسناد اولیه، اولویت با:

1. مخزن رسمی `vanhauser-thc/thc-hydra`
2. Help نسخه نصب‌شده Hydra
3. صفحه Hydra در Kali Linux
4. Source module upstream در صورت نیاز

## ساختار زبان‌ها

- فارسی: `docs/fa/`
- English: `docs/en/`
- نام فایل‌ها و شماره فصل‌ها باید متناظر بمانند.

## استاندارد مثال‌ها

فقط IP خصوصی آزمایشگاهی یا placeholder مستنداتی استفاده کنید. Credentialها مصنوعی باشند. هیچ Hostname واقعی شخص ثالث، Dump credential، Client data یا Output حساس وارد پروژه نکنید.

## بررسی محلی

```bash
python -m unittest discover -s scripts -p 'test_*.py'
python scripts/check_docs.py
mkdocs build --strict -f mkdocs.fa.yml
mkdocs build --strict -f mkdocs.en.yml
```

## محدوده

این Repository برای آموزش، Lab، Administration و ارزیابی امنیتی مجاز نگهداری می‌شود. تغییراتی که هدف اصلی آن‌ها دورزدن Lockout/MFA/CAPTCHA، پنهان‌سازی فعالیت یا سوءاستفاده خارج از Scope باشد پذیرفته نمی‌شوند.
