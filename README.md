# DELARCAD ASSOCIATE LIMITED — Website

A static, responsive marketing website for DELARCAD ASSOCIATE LIMITED, an
architecture and design practice. Built as plain HTML/CSS/JS with no build
step, so it deploys to Vercel as-is.

## Pages

- `index.html` — Home
- `about-us.html` — About Us (principals, culture, values)
- `about-delarcad.html` — The Practice (history, mission, track record)
- `resources.html` — Resources (guides, checklists & FAQ)
- `how-it-works.html` — How It Works (six-stage project process)
- `get-started.html` — Start a Project (intake form)
- `contact.html` — Contact (studio directory + message form)

## Structure

```
css/style.css   shared design tokens & styles
js/main.js      mobile nav toggle, active-link highlighting, client-side form handling
build.py, run_build.py, content_*.py   the Python build scripts used to generate
                                        the HTML pages (kept for future edits —
                                        not needed at runtime, safe to ignore
                                        or delete for deployment)
```

## Deploying to Vercel

This is a static site with no framework — in the Vercel dashboard, import
this repository and use:

- **Framework preset:** Other
- **Build command:** (none)
- **Output directory:** `.` (repo root)

## Before launch

- Replace the placeholder studio addresses, emails and phone numbers in
  `contact.html` and the footer with real ones.
- Wire the two forms (`get-started.html`, `contact.html`) to a real
  endpoint — e.g. Formspree, a Vercel serverless function, or a CRM. They
  currently intercept submission client-side in `js/main.js` and show a
  confirmation panel instead of sending anywhere.
- Swap the line-art hero illustration and project thumbnails in
  `index.html`/`about-delarcad.html` for real project photography once
  available.
- Replace the placeholder project names, dates and team bios throughout
  with real ones.
