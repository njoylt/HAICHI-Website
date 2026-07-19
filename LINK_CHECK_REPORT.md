# HAICHI Link Check Report

Date: 2026-07-19
Status: restored after verification

## Summary

Live `haichi.app` is reachable, core assets load, and both Lemon Squeezy checkout URLs now return `200 OK` during direct HTTP verification.

Public CTAs were restored to Lemon Squeezy checkout. The GitHub request/feedback form remains available for founder-code requests and support.

## Checked OK

- `https://haichi.app/`
- `https://haichi.app/haichi-app-logo.png`
- `https://haichi.app/styles.css`
- `https://haichi.app/haichi-product-overview.png`
- `https://haichi.app/haichi-collaboration.png`
- `https://haichi.app/app.js`
- `https://youtube.com/watch?v=US1zJvdP2c0`
- GitHub issue request form
- Page anchors:
  - `#main`
  - `#top`
  - `#features`
  - `#first-workflow`
  - `#security`
  - `#pricing`
  - `#faq`
  - `#download`

## Failed before restoration

- Personal Lemon Squeezy checkout: `404 Not Found`
- Developer Pro Lemon Squeezy checkout: `404 Not Found`

## Restored checkout

- Personal Lemon Squeezy checkout: `200 OK`
- Developer Pro Lemon Squeezy checkout: `200 OK`
- Founder code request: GitHub issue form

## Verified after restoration

- Request/feedback form: `200 OK`
- Public `haichi.lemonsqueezy.com/checkout` links are present again in `index.html`.
- Landing attribution is applied in `app.js` with `v1_1_verified_checkout`.

## Regression condition

Move public CTAs back to request-form fallback if:

1. Personal checkout URL returns 404 or fails in live checks.
2. Developer Pro checkout URL returns 404 or fails in live checks.
3. Lemon Squeezy delivery breaks.
4. Founder discount copy implies an automatic discount that is not configured.
