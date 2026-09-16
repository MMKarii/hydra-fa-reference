---
description: ثبت و گزارش نتیجه Hydra با وضعیت Validation، Evidence Hygiene و Context اصلاحی.
---
# خروجی و گزارش‌دهی

Output ابزار، Evidence است و Conclusion نهایی نیست. Report حرفه‌ای آنچه Hydra گفته را از آنچه مستقل تأیید شده جدا می‌کند.

## Procedure را ثبت کنید

- نسخه یا Header Help Hydra؛
- تاریخ و Scope؛
- Target آزمایشگاهی؛
- Service/Module؛
- Account و Candidate File مصنوعی؛
- کنترل دفاعی مرتبط؛
- Stop Condition و وضعیت Trigger آن.

## Result State

از وضعیت‌هایی مثل این استفاده کنید:

- **Confirmed** — موفقیت Authentication با حساب تست به‌طور ایمن تأیید شد؛
- **Possible / tool-reported** — Hydra Match احتمالی گزارش کرد ولی Validation مانده است؛
- **False positive** — Validation مستقل نتیجه را رد کرد؛
- **Control effective** — Lockout/Throttling/Blocking طبق طراحی عمل کرد.

## Remediation

Credential ضعیف آزمایشگاهی باید به Recommendation متناسب منجر شود: Password Policy، MFA، Rate Limit/Lockout، کاهش Exposure، Logging یا Alerting. Password واقعی را در Issue عمومی ثبت نکنید.
