---
description: Prepare synthetic Hydra username and password files for safe authentication labs.
---
# Credential input files

The supplied training notes use `users.txt` and `passwords.txt`. For a public training repository, those files should contain **synthetic values only**.

Example `users.txt`:

```text
labadmin
student1
service-test
```

Example `passwords.txt`:

```text
LabOnly-Weak-01
LabOnly-Weak-02
LabOnly-Control-03
```

## Input modes

Use a single login with `-l`, a login file with `-L`, a single password with `-p`, or a password file with `-P`. Upstream Hydra also supports paired login/password files with `-C`; consult `hydra -h` for the exact syntax on your installed version.

## Safe data handling

Do not populate training lists from password dumps, browser exports, client secrets, leaked credentials, production directory exports, or personal account data. If a test needs realistic policy characteristics, generate synthetic strings that exercise the same length/complexity rules.

## Design the lab around a test account

A dedicated test account should have an agreed password, known lockout threshold, and reset procedure. If the service uses real user accounts, treat that as a separate, higher-risk test requiring explicit authorization and a documented rollback plan.
