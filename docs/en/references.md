---
description: Source and technical references for the Hydra bilingual documentation project.
---
# References and review basis

## Project source material

The first edition is grounded in two Persian training documents supplied by the project maintainer. They cover installation, synthetic username/password files, SSH/FTP lab examples, HTTP/HTTPS form syntax, `F=` failure matching, false-positive risk, common defensive constraints, and explicit legal/ethical boundaries.

A real hostname that appeared in the original analysis document is intentionally **not reproduced** in this public repository.

## Primary external references

- [THC-Hydra upstream repository](https://github.com/vanhauser-thc/thc-hydra)
- [THC-Hydra upstream README](https://github.com/vanhauser-thc/thc-hydra/blob/master/README)
- [Hydra HTTP form module source](https://github.com/vanhauser-thc/thc-hydra/blob/master/hydra-http-form.c)
- [Kali Linux Hydra package documentation](https://www.kali.org/tools/hydra/)

## Review policy

When this project expands beyond the supplied training notes, the upstream Hydra source/help and Kali package documentation are used to verify technical claims. For exact behavior of a particular build, the installed `hydra -h` and module-specific `hydra -U <module>` output remain important version-specific references.
