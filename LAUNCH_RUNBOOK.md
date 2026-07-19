# HAICHI Launch Runbook

Date: 2026-07-19
Status: active working runbook

## Current public state

- Public site: `https://haichi.app`
- Positioning: local-first agent workspace for people already using Ollama/local AI tools.
- Primary workflow: `Reviewer -> Verifier -> Evidence Ready`
- Personal: free, no activation.
- Developer Pro: normal public price `€49`.
- Founder test: `€29` for first 10 useful Pro users via founder-code request.

## Current operational constraint

Lemon Squeezy checkout URLs returned `404 Not Found` in link verification. Public CTAs currently route to the GitHub request form instead of broken checkout pages.

Do not restore checkout links until they pass live verification.

## Daily launch loop

1. Check `https://haichi.app` loads.
2. Check the primary CTA works.
3. Check GitHub issues for:
   - download requests
   - founder code requests
   - install blockers
   - workflow feedback
4. Reply manually with:
   - Personal download path if available
   - founder code instructions if approved
   - a request for platform/error details if blocked
5. Track each lead in `FIRST_10_LEADS.md`.
6. Do not change product scope until at least 5 real users have responded or 1 user has paid.

## Safe outreach rule

Use one story only:

> HAICHI keeps local agent work inspectable: Reviewer finds risks, Verifier challenges them, you keep evidence-backed fixes.

Avoid:

- fake SaaS language
- login/account promises
- unsupported automation claims
- mass posting identical messages
- paid boosts before manual replies show interest

## Publish gate

Before broader posting:

- Personal request/download path must work.
- Pro/founder request path must work.
- Mobile page must not horizontally overflow.
- Checkout must not point to 404.
- One demo screenshot/GIF should be ready.
- Owner must approve paid ads or public mass posting.

## Commands

Website tests:

```powershell
cd C:\Users\tomas\Documents\HAICHI-Website
python -m unittest discover -s tests
```

Project smoke:

```powershell
cd C:\Users\tomas\Documents\ProjectHAICHI
.\.venv\Scripts\python.exe -m pytest tests/test_smoke.py -q
```

GitHub Pages status:

```powershell
cd C:\Users\tomas\Documents\HAICHI-Website
gh run list --limit 5 --json databaseId,name,status,conclusion,headSha,url
gh api repos/njoylt/HAICHI-Website/pages
```
