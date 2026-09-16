---
description: عیب‌یابی تست Hydra در Lab بدون تبدیل Failure به راهنمای Bypass یا Evasion.
---
# عیب‌یابی

هدف Troubleshooting این است که بفهمیم چرا Procedure آزمایشگاهی Application را درست مدل نمی‌کند؛ نه اینکه راه Bypass دفاع پیدا کنیم.

## مشکل SSH/FTP

Reachability، Service Availability، Module، Account مصنوعی و Authentication Method را بررسی کنید. Server Log مرجع اصلی علت است.

## مشکل Web Form

خطاهای رایج:

- Form Path اشتباه؛
- Field Name اشتباه؛
- Module HTTP/HTTPS اشتباه؛
- `F=` نامناسب؛
- Redirect مشابه برای همه پاسخ‌ها؛
- CSRF/Session Requirement؛
- Form مبتنی بر JavaScript پویا.

با Known-invalid Lab Login، Failure Response را مشخص کنید. اگر Application Dynamic State دارد که Hydra مدل نمی‌کند، تست را متوقف و Limit را مستند کنید.

## False Positive

اگر Hydra Match گزارش کرد، آن را با حساب Lab مستقل Validate کنید. نبود Failure String را به‌تنهایی Success ندانید.

## Escalation ممنوع

Failure تست را با Evasion، Anti-detection، CAPTCHA Bypass، MFA Bypass یا Lockout Bypass حل نکنید؛ این موارد خارج Scope پروژه هستند.
