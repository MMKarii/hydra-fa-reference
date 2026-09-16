---
description: منابع اولیه و فنی پروژه دو زبانه Hydra.
---
# منابع و مبنای بازبینی

## منابع اولیه پروژه

نسخه اول بر دو سند فارسی ارائه‌شده توسط Maintainer متکی است. موضوعات آن‌ها شامل نصب، فایل Username/Password مصنوعی، مثال SSH/FTP، Syntax فرم HTTP/HTTPS، `F=`، False Positive، محدودیت‌های دفاعی و مرز استفاده مجاز است.

Hostname واقعی موجود در یکی از اسناد اولیه عمداً در Repository عمومی **بازنشر نشده است**.

## منابع فنی اصلی

- [مخزن upstream THC-Hydra](https://github.com/vanhauser-thc/thc-hydra)
- [README رسمی upstream](https://github.com/vanhauser-thc/thc-hydra/blob/master/README)
- [Source ماژول HTTP Form](https://github.com/vanhauser-thc/thc-hydra/blob/master/hydra-http-form.c)
- [مستندات بسته Hydra در Kali Linux](https://www.kali.org/tools/hydra/)

## سیاست بازبینی

هر ادعایی که از دو سند اولیه فراتر رود با Source/Help upstream یا Kali بررسی می‌شود. برای رفتار دقیق یک Build خاص، `hydra -h` و `hydra -U <module>` روی همان سیستم مرجع مهمی هستند.
