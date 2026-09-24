# Portfolio + Resume — 3 Projects Design (2026-09-24)

## Goal
Add HealthQueue, Hostel_Management, E-commerce-Website with live + GitHub links to `index.html` and `resume.html`, maximize ATS parseability, regen PDF. No framework, no new deps.

## Context (verified)
- Single-file static `index.html` (543 lines), `PROJECTS` array lines 266-275 (8 entries), hero stats 8 shipped / 5 live.
- `resume.html` (78 lines) single-column Arial, standard headings, 8 project bullets, summary 8 shipped / 5 live.
- `check.py` guards: repos, lives, sections, keywords, no external JS, teal #2dd4bf / black #070b12, buttons, typed headline.
- Repos found: `HealthQueue` (Flask 3.0.3 + Flask-Login + SQLAlchemy, templates/static, vercel.json), `Hostel_Management` (flask + flask-login + flask-sqlalchemy, vercel.json), `E-commerce-Website` (vanilla HTML/CSS/JS + LocalStorage, ShopHub 16 products, cart/wishlist, 3-step checkout).
- Live (all 200 OK): https://healthqueue-nine.vercel.app/ , https://hostel-management-three-sigma.vercel.app/ , https://e-commerce-gilt-seven-90.vercel.app/
- Vercel project linked (`prj_fKjo2NWsnnNEba5L48TcGwni4hpm`); token NOT committed — push to origin, auto-deploy. Revoke token pasted in chat.

## Changes
### index.html
- Append 3 entries to `PROJECTS` (keep `name,repo,github,live,stack,blurb` shape; ICONS cycles `%8` so no new icons needed):
  - HealthQueue | `HealthQueue` | github.com/ansh012006/HealthQueue | healthqueue-nine.vercel.app | `Flask, Flask-Login, SQLAlchemy, Vercel` | `Patient/Doctor/Pharmacist appointments, availability, pharmacy, wait-time.`
  - Hostel Leave Management | `Hostel_Management` | github.com/ansh012006/Hostel_Management | hostel-management-three-sigma.vercel.app | `Flask, Flask-Login, SQLAlchemy, Vercel` | `Student leave apply, HOD/warden approve, gate IN/OUT, role dashboards.`
  - ShopHub E-Commerce | `E-commerce-Website` | github.com/ansh012006/E-commerce-Website | e-commerce-gilt-seven-90.vercel.app | `HTML/CSS/JS, LocalStorage, Vercel` | `16-product catalog, cart/wishlist, 3-step checkout, promo codes.`
- Hero stats: `8→11 projects shipped`, `5→8 live on Vercel`.
- ponytail: reuse slider/pager/ripple, no new CSS/JS libs.

### resume.html (ATS)
- Keep single-column, Arial, standard headings, no tables/graphics/columns.
- Summary: `8 shipped → 11 shipped`, `5 live → 8 live`, add `Flask-Login, SQLAlchemy, LocalStorage` keywords.
- Projects: append 3 one-line `<li>` with plain-text `Live: <url> | Code: <github>` (parseable, not link-only) + role/scale quantifiers.
- Keep ~1 page: 1 line per project, tight blurbs.
- Yes, live+GitHub per project maximizes ATS (recruiters + parsers extract URLs; plain text avoids link-only loss).

### PDF
- Regen `Ansh_Agarwal_Resume.pdf` via browser Print-to-PDF from updated `resume.html` (A4, 9mm margins). No python pdf lib.

## Non-goals
- No redeploy of the 3 project sites (already live). No portfolio redesign, no new pages/sections, no external assets, no emoji.

## Verification
- `python check.py` PASS (old asserts retained; new entries additive).
- Manual: open index.html, click 6 new buttons (3 Code + 3 Website), confirm 200.
- `git status/diff` review, push → Vercel auto-deploy; confirm live portfolio shows 11 slides.
- ATS: plain-text URLs present in resume.html, standard headings intact.

## Rollback
- Revert 2 files (`index.html`, `resume.html`) + PDF; Vercel auto-redeploys previous commit.
