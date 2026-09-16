---
description: ساختار دستور Hydra، ورودی Username/Password، Target و Service Module در محیط Lab.
---
# Syntax و ساختار دستور

اسناد اولیه ساختار کلاسیک را این‌طور معرفی می‌کنند:

```text
hydra [options] target service
```

upstream Hydra حالت URI-style نیز دارد، اما این مرجع در بیشتر مثال‌ها از ساختار کلاسیک استفاده می‌کند تا با منبع اولیه هماهنگ بماند.

## اجزای اصلی

| بخش | کاربرد |
|---|---|
| `hydra` | اجرای CLI |
| `-l LOGIN` | یک Login ثابت |
| `-L FILE` | فایل Loginها |
| `-p PASS` | یک Password ثابت |
| `-P FILE` | فایل Passwordها |
| `TARGET` | میزبان آزمایشگاهی داخل Scope |
| `SERVICE` | Module مانند `ssh` یا `ftp` |

مثال آزمایشگاهی:

```bash
hydra -l labadmin -P passwords.txt 192.168.56.10 ssh
```

نمونه با فایل Username:

```bash
hydra -L users.txt -P passwords.txt 192.168.56.20 ftp
```

## Module-specific Options

بعضی Moduleها Syntax اضافه دارند. فرم‌های HTTP نمونه مهم آن هستند و در [مبانی فرم HTTP/HTTPS](07-http-form-basics.md) بررسی می‌شوند. قبل از نوشتن Procedure از Help همان Module استفاده کنید:

```bash
hydra -U http-post-form
```

## Syntax با مجوز یکی نیست

درست بودن دستور از نظر فنی، مجوز اجرا ایجاد نمی‌کند. Target، Account، Candidate List و زمان اجرا باید داخل Scope تأییدشده باشند.
