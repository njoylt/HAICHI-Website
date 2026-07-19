# HAICHI Link Check Report

Date: 2026-07-19
Status: action taken

## Summary

Live `haichi.app` was reachable and core assets loaded, but both Lemon Squeezy checkout URLs returned `404 Not Found` during direct HTTP verification.

To avoid sending first users to broken checkout pages, public CTAs were changed to the GitHub request/feedback form until checkout delivery is restored and verified.

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

## Failed before fallback

- Personal Lemon Squeezy checkout: `404 Not Found`
- Developer Pro Lemon Squeezy checkout: `404 Not Found`

## Current fallback

- Personal download request: GitHub issue form
- Developer Pro request: GitHub issue form
- Founder code request: GitHub issue form

## Verified after fallback

- Request/feedback form: `200 OK`
- Personal download request form: `200 OK`
- Developer Pro request form: `200 OK`
- No public `haichi.lemonsqueezy.com/checkout` links remain in `index.html` or `app.js`.

## Restore condition

Only restore direct checkout links when:

1. Personal checkout URL returns a valid non-404 page.
2. Developer Pro checkout URL returns a valid non-404 page.
3. A founder discount/manual coupon path is confirmed.
4. A live smoke check confirms the final links from `https://haichi.app`.
