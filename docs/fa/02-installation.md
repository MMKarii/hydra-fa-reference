---
description: نصب و بررسی Hydra در Kali Linux برای آزمایشگاه کنترل‌شده.
---
# نصب و بررسی

اسناد اولیه از Kali Linux استفاده می‌کنند. Kali بسته `hydra` و در صورت نیاز بسته جداگانه `hydra-gtk` برای رابط گرافیکی را ارائه می‌کند.

## نصب

```bash
sudo apt update
sudo apt install hydra
```

رابط GTK را فقط در صورت نیاز نصب کنید:

```bash
sudo apt install hydra-gtk
```

## بررسی نصب

```bash
hydra -h
```

Help همان نسخه نصب‌شده، اولین مرجع Version-specific است. برای دیدن راهنمای یک Module نیز می‌توانید در Lab از این الگو استفاده کنید:

```bash
hydra -U ssh
```

اگر یک Module در Build موجود نیست، ممکن است وابستگی اختیاری آن هنگام Build فعال نشده باشد. برای نمونه، upstream برای ماژول SSH در Build-from-source به `libssh` اشاره می‌کند.

## Reproducibility

نسخه سیستم‌عامل، Header نسخه Hydra، Service مورد آزمون و نسخه Image آزمایشگاه را در گزارش ثبت کنید. Command یک محیط را بدون بررسی روی محیط دیگر تعمیم ندهید.

## عیب‌یابی نصب

اگر `hydra` پیدا نمی‌شود، تکمیل نصب Package و قرار داشتن Binary در `PATH` را بررسی کنید. برای نبودن یک Module، مستندات Kali یا Build upstream را بررسی کنید؛ مشکل نصب را با جایگزین کردن Target واقعی حل نکنید.
