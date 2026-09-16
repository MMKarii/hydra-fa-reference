---
description: برنامه‌ریزی ایمن تست Hydra با Scope، حساب تست، حجم کنترل‌شده و Stop Condition.
---
# اجرای ایمن در آزمایشگاه

حتی در Lab، آزمون احراز هویت می‌تواند Account Lockout و Telemetry پرحجم ایجاد کند. آن را مثل یک Change کنترل‌شده اجرا کنید.

## Pre-test Checklist

- Scope و مالکیت Target را تأیید کنید؛
- در صورت امکان Dedicated Test Account داشته باشید؛
- Candidate List مصنوعی باشد؛
- Lockout Threshold و Reset Step ثبت شود؛
- Owner یا Operator Lab مطلع باشد؛
- Stop Condition قبل از اجرا تعریف شود؛
- Server-side Log برای Validation جمع‌آوری شود.

## Request Volume هدفمند

صرفاً به دلیل کند بودن تست، Concurrency یا Retry را افزایش ندهید. هدف اثبات یک Security Property است، نه بیشینه کردن Attempt. از کوچک‌ترین Candidate Set کافی شروع کنید.

## محیط Production

تست Authentication در Production مجوز سخت‌گیرانه‌تری می‌خواهد چون می‌تواند کاربر واقعی را Lock کند یا Incident Response را فعال کند. این پروژه Tuning برای Credential Attempt پرحجم Production ارائه نمی‌دهد.

## Evidence Hygiene

فقط Evidence لازم را نگه دارید و Username نامرتبط، Token، Session ID، Inventory و داده حساس را قبل از Issue/Report عمومی Redact کنید.
