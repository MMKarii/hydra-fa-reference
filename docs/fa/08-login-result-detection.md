---
description: درک Failure/Success Matching فرم Hydra و جلوگیری از False Positive.
---
# تشخیص موفقیت و شکست ورود

مهم‌ترین نکته سند اولیه این است که Hydra بر اساس Match کردن پاسخ Server تصمیم می‌گیرد Attempt شکست خورده یا احتمالاً موفق بوده است.

## Failure Matching

با عبارت:

```text
F=incorrect
```

پاسخ‌هایی که `incorrect` دارند Failed تلقی می‌شوند. نبودن این متن می‌تواند بسته به Flow ماژول به‌عنوان موفقیت احتمالی دیده شود.

این موضوع **ریسک False Positive** ایجاد می‌کند. نبودن Failure String به‌تنهایی اثبات موفقیت Login نیست.

## علت‌های رایج Misclassification

- تغییر متن Error در Application؛
- Redirect یکسان برای همه Loginها؛
- پاسخ Generic از WAF/Reverse Proxy؛
- تفاوت Session State؛
- Field یا Endpoint اشتباه؛
- CSRF/Session Requirement که همه Requestهای Automation را نامعتبر می‌کند.

## Workflow اعتبارسنجی

با Credential آزمایشگاهی معلوم و اشتباه، Failure Response را مشخص کنید؛ سپس در صورت مجاز بودن، Known-good Lab Credential را برای Validation استفاده کنید. Server Log باید مرجع نهایی رفتار Application باشد.

## زبان گزارش

تا قبل از تأیید مستقل بنویسید «Hydra یک Credential Match احتمالی گزارش کرد». Tool Output را با Authentication Success تأییدشده یکی ندانید.
