---
description: مرجع حرفه‌ای فارسی Hydra برای ممیزی مجاز رمز عبور، آزمون احراز هویت آزمایشگاهی و اعتبارسنجی دفاعی.
---

<p class="project-banner"><img src="assets/brand-banner.webp" alt="بنر مرجع حرفه‌ای Hydra"></p>

<section class="hydra-hero">
  <span class="hero-kicker">Persian Hydra Reference</span>
  <h1>مرجع حرفه‌ای فارسی Hydra</h1>
  <p>مستند ساختارمند برای ممیزی مجاز رمز عبور، آزمون کنترل‌شده احراز هویت و اعتبارسنجی دفاعی. همه مثال‌ها از Credential مصنوعی و Target آزمایشگاهی استفاده می‌کنند.</p>
  <div class="hero-actions">
    <a class="primary" href="learning-path/">شروع مسیر یادگیری</a>
    <a href="cheatsheet/">Cheat Sheet</a>
    <a href="glossary/">واژه‌نامه</a>
    <a href="../en/">English</a>
    <a href="https://github.com/MMKarii/hydra-fa-reference">GitHub</a>
  </div>
</section>

!!! warning "فقط استفاده مجاز"
    Hydra را فقط روی سیستم شخصی، محیط آزمایشگاهی کنترل‌شده یا سامانه‌ای اجرا کنید که برای آزمون آن مجوز صریح دارید. این پروژه هیچ مجوزی برای آزمون سرویس شخص ثالث ایجاد نمی‌کند.

<div class="status-strip">
  <div class="status-item"><strong>۱۴ فصل</strong><span>از مبانی تا گزارش‌دهی و عیب‌یابی</span></div>
  <div class="status-item"><strong>Lab-only</strong><span>آدرس خصوصی و Credential مصنوعی</span></div>
  <div class="status-item"><strong>دفاعی</strong><span>Lockout، MFA، Rate Limiting، Monitoring و Validation</span></div>
  <div class="status-item"><strong>مبتنی بر منبع</strong><span>اسناد اولیه پروژه + منابع upstream Hydra/Kali</span></div>
</div>

## از کجا شروع کنم؟

<div class="docs-grid">
  <div class="docs-card"><h3><a href="learning-path/">مسیر یادگیری</a></h3><p>مسیر مبانی، آزمایشگاه یا اعتبارسنجی دفاعی را انتخاب کنید.</p></div>
  <div class="docs-card"><h3><a href="cheatsheet/">Cheat Sheet</a></h3><p>الگوهای امن آزمایشگاهی و قواعد Validation را سریع پیدا کنید.</p></div>
  <div class="docs-card"><h3><a href="references/">منابع فنی</a></h3><p>مخزن upstream Hydra و مستندات بسته Kali را بررسی کنید.</p></div>
</div>

## فصل‌ها

<div class="docs-grid">
  <div class="docs-card"><h3><a href="01-introduction/">۱. معرفی بنیادین</a></h3><p>Hydra چیست و آزمون مجاز احراز هویت چه جایگاهی دارد.</p></div>
  <div class="docs-card"><h3><a href="02-installation/">۲. نصب</a></h3><p>نصب در Kali، Help و بررسی پایه.</p></div>
  <div class="docs-card"><h3><a href="03-syntax/">۳. Syntax</a></h3><p>ساختار دستور، Target، Service و حالت‌های ورودی.</p></div>
  <div class="docs-card"><h3><a href="04-credential-inputs/">۴. Credential Inputs</a></h3><p>فایل‌های مصنوعی نام کاربری/رمز عبور و آماده‌سازی حساب تست.</p></div>
  <div class="docs-card"><h3><a href="05-ssh-lab/">۵. آزمایشگاه SSH</a></h3><p>ممیزی کنترل‌شده SSH با Stop Condition مشخص.</p></div>
  <div class="docs-card"><h3><a href="06-ftp-lab/">۶. آزمایشگاه FTP</a></h3><p>ممیزی کنترل‌شده FTP و مشاهده Logهای سمت سرور.</p></div>
  <div class="docs-card"><h3><a href="07-http-form-basics/">۷. فرم‌های HTTP/HTTPS</a></h3><p>ساختار ساده فرم با <code>^USER^</code>، <code>^PASS^</code> و شرط شکست.</p></div>
  <div class="docs-card"><h3><a href="08-login-result-detection/">۸. تشخیص نتیجه ورود</a></h3><p>Failure/Success Matching، False Positive و Validation مستقل.</p></div>
  <div class="docs-card"><h3><a href="09-protocol-overview/">۹. مرور پروتکل‌ها</a></h3><p>نمای مرجع‌محور از خانواده ماژول‌های رایج Hydra.</p></div>
  <div class="docs-card"><h3><a href="10-safe-lab-operation/">۱۰. اجرای ایمن Lab</a></h3><p>Scope، حساب تست، حجم درخواست و Stop Condition.</p></div>
  <div class="docs-card"><h3><a href="11-output-reporting/">۱۱. خروجی و گزارش</a></h3><p>Evidence، وضعیت تأیید و توصیه اصلاحی.</p></div>
  <div class="docs-card"><h3><a href="12-defensive-controls/">۱۲. کنترل‌های دفاعی</a></h3><p>Rate Limit، Lockout، MFA، CAPTCHA، CSRF و Monitoring.</p></div>
  <div class="docs-card"><h3><a href="13-troubleshooting/">۱۳. عیب‌یابی</a></h3><p>Path، Field، Failure String، Redirect، CSRF و False Positive.</p></div>
  <div class="docs-card"><h3><a href="14-common-mistakes/">۱۴. اشتباهات رایج</a></h3><p>خطاهای Scope، Credential و تفسیر نتیجه.</p></div>
</div>
