---
description: کنترل‌های دفاعی مرتبط با Hydra شامل MFA، Rate Limiting، Lockout، CAPTCHA، CSRF و Monitoring.
---
# کنترل‌های دفاعی

اسناد اولیه CAPTCHA، CSRF Token، Rate Limiting و IP Blocking/Greylisting را به‌عنوان محدودیت‌های عملی ذکر می‌کنند. این‌ها بخشی از دفاع گسترده‌تر Authentication هستند.

## Rate Limiting و Lockout

Rate Limiting سرعت Attemptهای تکراری را محدود می‌کند. Lockout می‌تواند Failureهای تکراری را متوقف کند، اما باید طوری طراحی شود که Denial-of-Service روی حساب کاربر آسان نشود. Security Effect و Recovery Process را هر دو تست کنید.

## MFA

MFA با افزودن Factor دیگر، ارزش یک Password افشاشده را کاهش می‌دهد. این پروژه روش MFA Bypass آموزش نمی‌دهد؛ Flow محافظت‌شده با MFA به‌عنوان Control دفاعی ارزیابی می‌شود.

## CAPTCHA و Anti-automation

CAPTCHA می‌تواند Login Automation را مختل کند. در Assessment مجاز، Coverage و رفتار Control را مستند کنید؛ این مرجع برای شکست دادن آن طراحی نشده است.

## CSRF و Session

CSRF Token هدف اصلی دیگری دارد، اما Dynamic Session State می‌تواند Replay ساده را نیز نامعتبر کند. شکست یک تعریف ساده Hydra به‌تنهایی ثابت نمی‌کند Authentication قوی یا ضعیف است.

## Monitoring و Alerting

Failureهای تکراری، Source، Account، Window زمانی و Success پس از Failure Burst را Correlate کنید. Log نباید Full Password یا Session Secret حساس را ذخیره کند.
