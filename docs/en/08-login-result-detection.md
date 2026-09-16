---
description: Understand Hydra form failure/success matching and prevent false-positive authentication findings.
---
# Login result detection

The source material highlights the most important web-form lesson: Hydra decides whether an attempt failed or might have succeeded by matching response content.

## Failure matching

With:

```text
F=incorrect
```

Hydra treats responses containing `incorrect` as failed. If that text is absent, the result may be treated as a possible success depending on the module flow.

That creates a **false-positive risk**. A missing failure string does not prove authentication succeeded.

## Common reasons for misclassification

- the application changed its error wording;
- all attempts redirect to the same page;
- a reverse proxy or WAF returns a generic response;
- session state changes the response body;
- the application uses a different field name or endpoint;
- CSRF/session requirements make every automated request invalid.

## Validation workflow

Use a known-bad synthetic credential to capture the failure behavior in the lab, configure the matching condition, and then test against a known-good lab credential only if that step is explicitly part of the exercise. Review server-side logs to confirm what the application actually did.

## Reporting language

Write "Hydra reported a possible credential match" until the result is independently confirmed. A defensible report distinguishes tool output from validated authentication success.
