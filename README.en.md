<p align="center">
  <img src="docs/en/assets/brand-banner.webp" alt="Hydra Reference" width="100%">
</p>

<p align="center"><a href="README.md">Language selection</a> · <a href="README.fa.md">فارسی</a></p>

<h1 align="center">Hydra Professional Reference</h1>

<p align="center">Structured documentation for learning Hydra, authorized authentication auditing, controlled lab practice, and defensive validation.</p>

<p align="center">
  <a href="docs/en/index.md">Read the English edition</a> ·
  <a href="docs/en/learning-path.md">Learning Path</a> ·
  <a href="docs/en/cheatsheet.md">Cheat Sheet</a> ·
  <a href="docs/en/references.md">Technical References</a> ·
  <a href="LICENSE">License</a>
</p>

> [!IMPORTANT]
> Use Hydra only on systems you own, controlled training labs, or systems you are explicitly authorized to assess. No example in this project targets a real third party.

## About the project

The source material covers Hydra installation, username/password files, SSH and FTP lab use, HTTP/HTTPS form syntax, `F=` failure detection, false positives, and defensive constraints such as CSRF, CAPTCHA, and rate limiting. Technical expansion is checked against authoritative Hydra and Kali sources.

## Chapters

| Chapter | Topic |
|---:|---|
| 1 | [Hydra Fundamentals](docs/en/01-introduction.md) |
| 2 | [Installation and Verification](docs/en/02-installation.md) |
| 3 | [Syntax and Command Structure](docs/en/03-syntax.md) |
| 4 | [Credential Input Files](docs/en/04-credential-inputs.md) |
| 5 | [SSH Lab](docs/en/05-ssh-lab.md) |
| 6 | [FTP Lab](docs/en/06-ftp-lab.md) |
| 7 | [HTTP/HTTPS Form Basics](docs/en/07-http-form-basics.md) |
| 8 | [Login Result Detection](docs/en/08-login-result-detection.md) |
| 9 | [Protocol Overview](docs/en/09-protocol-overview.md) |
| 10 | [Safe Lab Operation](docs/en/10-safe-lab-operation.md) |
| 11 | [Output and Reporting](docs/en/11-output-reporting.md) |
| 12 | [Defensive Controls](docs/en/12-defensive-controls.md) |
| 13 | [Troubleshooting](docs/en/13-troubleshooting.md) |
| 14 | [Common Mistakes](docs/en/14-common-mistakes.md) |

## Lab-only quick start

```bash
hydra -l labadmin -P passwords.txt 192.168.56.10 ssh
```

Use a dedicated test account and synthetic wordlist, and define lockout policy and stopping conditions before testing.

## License

Original project documentation is CC BY 4.0. Upstream Hydra remains a separate project with its own license and rights.
