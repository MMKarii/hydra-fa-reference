---
description: اشتباهات رایج Hydra در Scope، Credential، Result Interpretation و کنترل‌های دفاعی.
---
# اشتباهات رایج

## Syntax را مجوز فرض کردن

Working Command به معنی Permission نیست. Target، Account، Window و Candidate Data باید داخل Scope باشند.

## استفاده از Credential واقعی

Documentation عمومی نباید Password مشتری، Leak، Browser Export، Token یا Credential Production داشته باشد. از داده مصنوعی استفاده کنید.

## کپی کردن Target واقعی

یکی از اسناد اولیه یک Hostname واقعی داشت. این پروژه عمومی عمداً آن را با IP آزمایشگاهی جایگزین کرده است. Target واقعی را در Issue، PR، Screenshot یا Example برنگردانید.

## برداشت اشتباه از `F=`

`F=incorrect` Rule تطبیق Response است. نبود آن Proof of Success نیست. Match احتمالی را مستقل Validate کنید.

## نادیده گرفتن Lockout

Attempt تکراری حتی حساب Test را Lock می‌کند. Threshold و Reset Path را قبل از اجرا بدانید.

## کنترل دفاعی را مانع تلقی کردن

CAPTCHA، MFA، CSRF/Session، Throttling و Blocking باید مستند و اعتبارسنجی شوند؛ این پروژه Bypass آن‌ها را آموزش نمی‌دهد.

## Report بدون Context

Version، Module، Target Lab، Candidate Source، Control Behavior و Validation Status را ثبت کنید تا Tester مجاز دیگر بتواند نتیجه را تکرار کند.
