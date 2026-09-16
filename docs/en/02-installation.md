---
description: Install and verify Hydra on Kali Linux for a controlled lab.
---
# Installation and verification

The supplied training notes use Kali Linux. Kali currently provides the `hydra` package and a separate `hydra-gtk` package for the graphical frontend.

## Install

```bash
sudo apt update
sudo apt install hydra
```

Install the optional GTK frontend only when you actually need it:

```bash
sudo apt install hydra-gtk
```

## Verify

```bash
hydra -h
```

The help output is the first version-specific reference for the binary you installed. For a module-specific summary, use a controlled module name:

```bash
hydra -U ssh
```

If a module is absent, the binary may have been built without an optional dependency. The upstream source documents, for example, that SSH support depends on `libssh` when building from source.

## Keep the lab reproducible

Record the operating system, Hydra version/help header, service under test, and lab image version in your notes. Do not assume a command copied from another environment has identical module support.

## Troubleshooting installation

If `hydra` is not found after installation, verify that the package installation completed and that the binary is on your shell `PATH`. If a specific module is unavailable, compare the installed build with the Kali package page or upstream build requirements rather than substituting a different real-world target.
