---
description: Bilingual-ready English Hydra reference for authorized password auditing, authentication testing, controlled labs, and defensive validation.
---

<p class="project-banner"><img src="assets/brand-banner.webp" alt="Hydra Professional Reference banner"></p>

<section class="hydra-hero">
  <span class="hero-kicker">English Hydra Reference</span>
  <h1>Hydra Professional Reference</h1>
  <p>Structured documentation for authorized password auditing, controlled authentication testing, and defensive validation. Every command in this edition uses synthetic credentials and lab-only targets.</p>
  <div class="hero-actions">
    <a class="primary" href="learning-path/">Start the learning path</a>
    <a href="cheatsheet/">Cheat Sheet</a>
    <a href="glossary/">Glossary</a>
    <a href="../fa/">فارسی</a>
    <a href="https://github.com/MMKarii/hydra-fa-reference">GitHub</a>
  </div>
</section>

!!! warning "Authorized use only"
    Run Hydra only against systems you own, controlled training labs, or systems you are explicitly authorized to assess. This project does not authorize testing third-party services.

<div class="status-strip">
  <div class="status-item"><strong>14 chapters</strong><span>Fundamentals through reporting and troubleshooting</span></div>
  <div class="status-item"><strong>Lab-only</strong><span>Private test addresses and synthetic credentials</span></div>
  <div class="status-item"><strong>Defensive</strong><span>Lockout, MFA, rate limiting, monitoring, and validation</span></div>
  <div class="status-item"><strong>Source-grounded</strong><span>Maintainer notes plus upstream Hydra/Kali references</span></div>
</div>

## Where should I start?

<div class="docs-grid">
  <div class="docs-card"><h3><a href="learning-path/">Learning Path</a></h3><p>Choose a foundation, lab, or defensive-validation sequence.</p></div>
  <div class="docs-card"><h3><a href="cheatsheet/">Cheat Sheet</a></h3><p>Quickly recall safe lab command patterns and result checks.</p></div>
  <div class="docs-card"><h3><a href="references/">Technical References</a></h3><p>Review the upstream Hydra repository and Kali package documentation.</p></div>
</div>

## Chapters

<div class="docs-grid">
  <div class="docs-card"><h3><a href="01-introduction/">1. Fundamentals</a></h3><p>What Hydra does and where authorized authentication testing fits.</p></div>
  <div class="docs-card"><h3><a href="02-installation/">2. Installation</a></h3><p>Kali installation, help output, and basic verification.</p></div>
  <div class="docs-card"><h3><a href="03-syntax/">3. Syntax</a></h3><p>Command structure, targets, services, and input modes.</p></div>
  <div class="docs-card"><h3><a href="04-credential-inputs/">4. Credential Inputs</a></h3><p>Synthetic username/password files and safe test-account preparation.</p></div>
  <div class="docs-card"><h3><a href="05-ssh-lab/">5. SSH Lab</a></h3><p>Controlled SSH authentication auditing with explicit stopping conditions.</p></div>
  <div class="docs-card"><h3><a href="06-ftp-lab/">6. FTP Lab</a></h3><p>Controlled FTP authentication auditing and server-side observations.</p></div>
  <div class="docs-card"><h3><a href="07-http-form-basics/">7. HTTP Forms</a></h3><p>Simple form structure with <code>^USER^</code>, <code>^PASS^</code>, and a failure condition.</p></div>
  <div class="docs-card"><h3><a href="08-login-result-detection/">8. Result Detection</a></h3><p>Failure/success matching, false positives, and independent validation.</p></div>
  <div class="docs-card"><h3><a href="09-protocol-overview/">9. Protocol Overview</a></h3><p>Reference-oriented view of common Hydra module families.</p></div>
  <div class="docs-card"><h3><a href="10-safe-lab-operation/">10. Safe Lab Operation</a></h3><p>Scope, test accounts, request restraint, and stop conditions.</p></div>
  <div class="docs-card"><h3><a href="11-output-reporting/">11. Output & Reporting</a></h3><p>Evidence handling, confirmed findings, and remediation notes.</p></div>
  <div class="docs-card"><h3><a href="12-defensive-controls/">12. Defensive Controls</a></h3><p>Rate limiting, lockout, MFA, CAPTCHA, CSRF, and monitoring.</p></div>
  <div class="docs-card"><h3><a href="13-troubleshooting/">13. Troubleshooting</a></h3><p>Wrong fields, failure strings, redirects, CSRF, reachability, and false positives.</p></div>
  <div class="docs-card"><h3><a href="14-common-mistakes/">14. Common Mistakes</a></h3><p>Unsafe scope assumptions and common interpretation errors.</p></div>
</div>
