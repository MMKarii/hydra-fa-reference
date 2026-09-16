<p align="center">
  <img src="docs/fa/assets/brand-banner.webp" alt="Hydra Professional Reference" width="100%">
</p>

<p align="center">
  <a href="https://github.com/MMKarii/hydra-fa-reference/actions/workflows/docs.yml"><img src="https://github.com/MMKarii/hydra-fa-reference/actions/workflows/docs.yml/badge.svg" alt="Docs build"></a>
  <a href="docs/fa/index.md"><img src="https://img.shields.io/badge/docs-فارسی-239f40" alt="Persian docs"></a>
  <a href="docs/en/index.md"><img src="https://img.shields.io/badge/docs-English-0284c7" alt="English docs"></a>
  <a href="https://github.com/vanhauser-thc/thc-hydra"><img src="https://img.shields.io/badge/reference-THC--Hydra-b91c1c" alt="Official THC-Hydra repository"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC%20BY%204.0-6b7280" alt="CC BY 4.0"></a>
</p>

<h1 align="center">Hydra Professional Reference · مرجع حرفه‌ای Hydra</h1>

<p align="center">Bilingual Persian and English documentation for authorized password auditing, authentication testing, lab practice, and defensive validation.</p>
<p align="center">مستند دو زبانه فارسی و انگلیسی برای ممیزی مجاز رمز عبور، آزمون احراز هویت، تمرین آزمایشگاهی و اعتبارسنجی دفاعی.</p>

<table align="center">
<tr>
<td align="center" width="50%">
<h2>فارسی</h2>
<p>نسخه کامل RTL با ۱۴ فصل، مسیر یادگیری، Cheat Sheet و منابع فنی.</p>
<p><a href="docs/fa/index.md"><strong>مطالعه نسخه فارسی</strong></a></p>
<p><a href="README.fa.md">README فارسی</a></p>
</td>
<td align="center" width="50%">
<h2>English</h2>
<p>Complete LTR edition with 14 chapters, learning paths, a cheat sheet, and technical references.</p>
<p><a href="docs/en/index.md"><strong>Read the English edition</strong></a></p>
<p><a href="README.en.md">English README</a></p>
</td>
</tr>
</table>

> [!IMPORTANT]
> Use Hydra only on systems you own, controlled training labs, or systems for which you have explicit authorization. تمام مثال‌های این پروژه فقط برای محیط شخصی، آزمایشگاهی یا ارزیابی دارای مجوز هستند.

## Project structure

```text
.
├── docs/
│   ├── fa/                 # Persian / RTL edition
│   └── en/                 # English / LTR edition
├── mkdocs.fa.yml
├── mkdocs.en.yml
├── site-root/index.html
├── README.fa.md
├── README.en.md
├── LICENSE
└── .github/workflows/docs.yml
```

Both editions use matching chapter numbers and filenames. The documentation is source-grounded in the uploaded Hydra training material and technically extended only with authoritative Hydra/Kali references.

## Lab-only quick example

```bash
hydra -l labadmin -P passwords.txt 192.168.56.10 ssh
```

Use a dedicated test account and synthetic password list in a controlled lab. Avoid production accounts, real credential collections, and unauthorized targets.

## License

Original project documentation is released under the Creative Commons Attribution 4.0 International license. See [LICENSE](LICENSE). THC-Hydra itself is an upstream third-party project with its own license and rights.
