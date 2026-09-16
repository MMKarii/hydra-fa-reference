---
description: Controlled Hydra SSH password-auditing lab using a synthetic account and private test address.
---
# SSH lab

This chapter adapts the supplied SSH example to an isolated test network.

## Lab setup

Use a dedicated SSH server at `192.168.56.10`, a synthetic account such as `labadmin`, and a short password file created for the exercise. Confirm the service owner knows the test window and lockout behavior.

```bash
hydra -l labadmin -P passwords.txt 192.168.56.10 ssh
```

Parameter meaning:

- `-l labadmin` fixes one synthetic login name;
- `-P passwords.txt` supplies the lab candidate list;
- `192.168.56.10` is a private lab target;
- `ssh` selects the SSH module.

## Observe the defensive side

While the test runs, monitor the SSH authentication log, account lockout state, alerting pipeline, and any source-IP throttling. The goal is not only to see whether a weak credential can be identified; it is also to validate the defensive telemetry and response.

## Stop conditions

Stop immediately if the test account locks unexpectedly, the host becomes unstable, authentication latency rises materially, or the activity leaves the agreed lab scope. Do not respond by adding bypass, evasion, or higher-volume options.

## Validate findings

Treat a reported credential as a finding that still requires safe confirmation. Validate with the approved test account and then reset the credential after the exercise.
