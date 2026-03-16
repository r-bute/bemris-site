# Bemris Site

Bemris is a static marketing site hosted on GitHub Pages with a dedicated Salesforce-focused landing page.

This repository includes:
- the main site entry pages
- the compiled frontend bundle in `assets/`
- a standalone Salesforce landing page
- simple local preview servers
- maintenance documentation for the Salesforce page

## Live Site Structure

Primary entry pages:
- `index.html`
- `about.html`
- `services.html`
- `contact.html`
- `testimonials.html`
- `salesforce-admin.html`
- `404.html`

Static assets:
- `assets/index-D2RM8O5o.js`
- `assets/index-BxS1wpav.css`
- `assets/bemris logo_1752973993415-jtu8LomD.png`

Local tooling:
- `serve.py`
- `local-server.js`

Documentation:
- `LOCAL_DEVELOPMENT_GUIDE.md`
- `SALESFORCE_PAGE_README.md`

## What Is Special About This Repo

This repo is not a typical source-code-plus-build-output project.

Important details:
- the main site is currently shipped as static HTML entry pages plus a compiled JavaScript bundle
- some content updates are made directly in checked-in HTML files
- some text in the main site still lives inside the built file `assets/index-D2RM8O5o.js`
- the Salesforce page is a standalone HTML page and is much easier to edit directly

Because of that, some edits are straightforward and some are not.

## Main Pages

### Main site

The main Bemris pages use:
- individual HTML entry files like `about.html`
- the compiled app bundle loaded from `assets/index-D2RM8O5o.js`

The following files help those pages load the correct route before the app starts:
- `about.html`
- `services.html`
- `contact.html`
- `testimonials.html`

Those files contain small `window.history.replaceState(...)` fixes so the app sees clean routes like `/about` instead of `/about.html`.

### Salesforce landing page

The file:
- `salesforce-admin.html`

is a standalone page for Salesforce freelance lead generation.

It includes:
- custom page design and CSS
- SEO metadata
- structured data
- a custom lead form
- GA4 tracking events

If you need to edit that page often, start here:
- `SALESFORCE_PAGE_README.md`

## Local Development

Use one of the included local preview servers.

### Option 1: Python

```bash
python3 serve.py
```

Then visit:
- `http://localhost:8000/`
- `http://localhost:8000/about`
- `http://localhost:8000/services`
- `http://localhost:8000/contact`
- `http://localhost:8000/testimonials`
- `http://localhost:8000/salesforce-admin`

### Option 2: Node

```bash
npm install express
node local-server.js
```

Then visit:
- `http://localhost:3000`

More details:
- `LOCAL_DEVELOPMENT_GUIDE.md`

## Editing Guide

### Easy edits

These are simple to update directly:
- `salesforce-admin.html`
- metadata in the top of each HTML file
- route links between static pages
- Google Analytics snippets in the HTML files

### Harder edits

These are harder because they live inside a compiled bundle:
- some main-site content text
- some footer content
- some form logic and page rendering in the main site

That work currently happens in:
- `assets/index-D2RM8O5o.js`

If you only need small text tweaks there, direct edits are possible but not ideal.

## Form Handling

The Salesforce page form:
- does not use a custom backend
- submits to Google Forms using JavaScript

Current form endpoint:
- `https://docs.google.com/forms/d/YOUR_FORM_ID/formResponse`

The visible form lives in:
- `salesforce-admin.html`

For exact field mapping and editing instructions:
- `SALESFORCE_PAGE_README.md`

## Analytics

Google Analytics 4 is installed on the site with the GA4 measurement ID:
- `G-XXXXXXXXXX`

GA4 is included in:
- `index.html`
- `about.html`
- `services.html`
- `contact.html`
- `testimonials.html`
- `404.html`
- `salesforce-admin.html`

Custom event tracking currently exists on the Salesforce page for:
- email clicks
- CTA clicks
- form submissions

Tracked event names:
- `salesforce_email_click`
- `salesforce_cta_click`
- `salesforce_form_submit`

## SEO

The Salesforce page has a stronger SEO setup than the rest of the site.

It includes:
- targeted title and meta description
- canonical tag
- Open Graph tags
- Twitter tags
- JSON-LD structured data

That configuration lives in:
- `salesforce-admin.html`

## Deployment

This repo is intended for GitHub Pages.

Helpful files:
- `CNAME`
- `404.html`

Notes:
- changes pushed to `main` usually go live within a few minutes
- browser caching can delay what you see locally after deploy
- a hard refresh or private window is useful when checking updates

## Recommended Maintenance Workflow

1. Edit the file you need
2. Preview locally with `serve.py` or `local-server.js`
3. Test the affected page and links
4. Test form submissions if the form changed
5. Commit the changes
6. Push to `main`
7. Wait for GitHub Pages to update

## Files Worth Knowing

- `salesforce-admin.html`
  Purpose: Salesforce lead-generation landing page

- `SALESFORCE_PAGE_README.md`
  Purpose: deep editing guide for the Salesforce page

- `LOCAL_DEVELOPMENT_GUIDE.md`
  Purpose: local preview instructions

- `serve.py`
  Purpose: simple Python local route server

- `local-server.js`
  Purpose: simple Node/Express local route server

- `assets/index-D2RM8O5o.js`
  Purpose: compiled main frontend bundle

- `assets/index-BxS1wpav.css`
  Purpose: compiled stylesheet

## Notes For Future Cleanup

If this site grows, the next improvements would be:
- move the main site out of compiled-only editing
- keep source code and build output separate
- add a cleaner content-editing workflow
- centralize shared metadata and analytics setup

For now, this repo is fully workable as-is, but the Salesforce page is the easiest place to make ongoing business-facing updates.
