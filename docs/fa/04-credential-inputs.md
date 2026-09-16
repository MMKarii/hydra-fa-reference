---
description: آماده‌سازی فایل مصنوعی Username و Password برای آزمایشگاه ایمن Hydra.
---
# ورودی‌های نام کاربری و رمز عبور

اسناد اولیه از `users.txt` و `passwords.txt` استفاده می‌کنند. در Repository عمومی، این فایل‌ها باید **کاملاً مصنوعی** باشند.

نمونه `users.txt`:

```text
labadmin
student1
service-test
```

نمونه `passwords.txt`:

```text
LabOnly-Weak-01
LabOnly-Weak-02
LabOnly-Control-03
```

## حالت‌های ورودی

`-l` برای یک Login، `-L` برای فایل Login، `-p` برای یک Password و `-P` برای فایل Password است. upstream گزینه `-C` را نیز برای Pairهای Login/Password مستند کرده است؛ Syntax دقیق نسخه نصب‌شده را با `hydra -h` بررسی کنید.

## Hygiene داده

از Password Dump، Export مرورگر، Secret مشتری، Credential Leak، Directory Export تولید یا حساب شخصی برای ساخت Wordlist آموزشی استفاده نکنید. اگر لازم است ویژگی‌های Policy واقعی شبیه‌سازی شود، String مصنوعی با همان Length/Complexity بسازید.

## حساب تست

حساب آزمایشگاهی باید Password معلوم، Threshold Lockout معلوم و روش Reset مشخص داشته باشد. تست روی حساب کاربران واقعی نیازمند مجوز جداگانه و برنامه Rollback روشن است.
