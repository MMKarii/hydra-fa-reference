---
description: Hydra command structure, login/password inputs, targets, and service modules for lab use.
---
# Syntax and command structure

The maintainer notes introduce the classic form:

```text
hydra [options] target service
```

Upstream Hydra also documents a URI-style form. This reference uses the classic style in most examples because it matches the supplied material and keeps the target/service relationship obvious.

## Core pieces

| Part | Purpose |
|---|---|
| `hydra` | Run the CLI |
| `-l LOGIN` | One login value |
| `-L FILE` | Login list file |
| `-p PASS` | One password value |
| `-P FILE` | Password list file |
| `TARGET` | In-scope lab host |
| `SERVICE` | Module such as `ssh` or `ftp` |

Lab-only example:

```bash
hydra -l labadmin -P passwords.txt 192.168.56.10 ssh
```

The same structure with a login list is:

```bash
hydra -L users.txt -P passwords.txt 192.168.56.20 ftp
```

## Module-specific options

Some modules require extra syntax. HTTP form modules are a key example and are covered in [HTTP/HTTPS form basics](07-http-form-basics.md). Use the installed module help before writing an assessment procedure:

```bash
hydra -U http-post-form
```

## Keep syntax separate from authorization

A syntactically valid command is not automatically an authorized command. The target, account, candidate list, and timing must all be within the approved scope.
