# Security Policy

## Reporting a vulnerability

Please report security issues privately — **do not** open a public GitHub issue.

Email **[senyao@polyvia.ai](mailto:senyao@polyvia.ai)** with:

- A description of the issue and its potential impact.
- Steps to reproduce (a minimal proof-of-concept if possible).
- Any relevant logs or requests, with API keys and personal data redacted.

We aim to acknowledge reports within 2 business days and will keep you updated as
we investigate and ship a fix. We're happy to credit reporters who'd like it.

## Handling secrets

- API keys are bound to a single workspace and start with `poly_`.
- Never commit keys or customer data. Keep keys in environment variables
  (`POLYVIA_API_KEY`) and out of client-side code and public repos.
- Revoke and re-mint a key any time in **Settings → API** at
  [app.polyvia.ai](https://app.polyvia.ai).

## Enterprise & data residency

For regulated deployments, Polyvia can run **on-prem / in your own VPC** so
documents never leave your systems. Contact [senyao@polyvia.ai](mailto:senyao@polyvia.ai).
