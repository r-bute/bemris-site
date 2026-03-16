# Salesforce Page Editing Guide

This file explains how to update the Salesforce landing page and the supporting files around it.

Main file:
- `salesforce-admin.html`

Supporting files that affect related behavior:
- `about.html`
- `services.html`
- `contact.html`
- `testimonials.html`
- `assets/index-D2RM8O5o.js`

## What This Page Is For

The page at `salesforce-admin.html` is a dedicated landing page for Salesforce freelance work.

It is designed to:
- rank for Salesforce admin-related searches
- give you a focused page to send to leads
- collect inquiries through the same Google Form backend used by the main site

## Quick Edit Map

Use this section if you just want to know where to change something.

- SEO title and description:
  `salesforce-admin.html` inside `<head>`

- Social preview text:
  `salesforce-admin.html` inside Open Graph and Twitter meta tags

- Structured data:
  `salesforce-admin.html` inside `<script type="application/ld+json">`

- Logo and top-left navigation:
  `salesforce-admin.html` inside `.topbar`

- Main headline and intro copy:
  `salesforce-admin.html` inside the `.hero` section

- Services cards:
  `salesforce-admin.html` inside the first `.section-grid`

- Client-fit cards:
  `salesforce-admin.html` inside `.fit-grid`

- Form fields and labels:
  `salesforce-admin.html` inside `<form id="salesforce-support-form">`

- Form submission behavior:
  `salesforce-admin.html` inside the bottom `<script>`

- Footer text:
  `salesforce-admin.html` inside `<footer>`

- Main site footer text:
  `assets/index-D2RM8O5o.js`

## Editing The SEO Section

At the top of `salesforce-admin.html`, update these when needed:

- `<title>`
- `<meta name="description">`
- `<link rel="canonical">`
- `og:title`
- `og:description`
- `og:url`
- `twitter:title`
- `twitter:description`

Use this area when:
- you want to change the target keyword
- you want to change the page title shown in Google
- you want to improve social sharing previews

Good keyword phrases for this page:
- `Freelance Salesforce Administrator`
- `Salesforce Admin support`
- `Certified Salesforce Administrator`
- `Contract Salesforce Admin`

Try to keep the title natural. Do not repeat the same phrase too many times.

## Editing The Structured Data

Inside the JSON-LD block in `salesforce-admin.html`, you can update:

- `name`
- `url`
- `image`
- `description`
- `areaServed`
- `serviceType`
- `email`

Use this if:
- your service offer changes
- you want to add or remove service types
- your public email changes

Be careful:
- keep valid JSON formatting
- use double quotes only
- do not leave trailing commas

## Editing The Top Bar

The top bar includes:
- the Bemris logo
- the `Back to Bemris` link

Look for:
- `.brand-row`
- `.brand-mark`
- `.crumb`

To change the logo image:
- update the `src` on the `<img>` tag

Current logo file:
- `/assets/bemris logo_1752973993415-jtu8LomD.png`

## Editing The Main Hero

The hero section contains:
- the small certification tag
- the main headline
- the intro paragraphs
- the main CTAs

Look for:
- `<div class="eyebrow">`
- `<h1>`
- `<p class="lead">`
- `<div class="hero-actions">`

Use this area when:
- you want to change your positioning
- you gain more experience or certifications
- you want to target a different kind of client

Examples of easy updates:
- change `2 years` to your current experience
- update wording from `Administrator` to `Admin Consultant` if your positioning changes
- change CTA labels

## Editing The Service Sections

There are several content blocks after the hero:

1. `How I can help as a freelance Salesforce Administrator`
2. `What Salesforce Admin clients usually need`
3. `Why this offer is focused`
4. `Need a freelance Salesforce Administrator without hiring full-time yet?`
5. `Ideal fit for freelance Salesforce Admin support`

To update these:
- edit the `<h2>`, `<h3>`, `<p>`, and `<li>` text directly in `salesforce-admin.html`

Use these sections to:
- add new services
- remove services you do not offer
- change your ideal client type
- update your experience or certification story

## Editing The Form

The visible form is in `salesforce-admin.html`.

Look for:
- `<form id="salesforce-support-form">`

Current visible fields:
- First Name
- Last Name
- Email
- Company
- Service Interest
- Message

To change labels or placeholders:
- edit the `<label>` text
- edit each field `placeholder`

To change service options:
- edit the `<option>` values inside the `select`

## How Form Submission Works

The page does not use a backend server.

It sends form data directly to Google Forms using JavaScript in the bottom `<script>` block.

Current Google Form endpoint:
- `https://docs.google.com/forms/d/1SC_Hs6NaBEIeRmDZwCG0SYgVR47IPHpbqLPTLGx7lbI/formResponse`

Current field mapping:
- full name -> `entry.286016800`
- email -> `emailAddress`
- service interest -> `entry.342022558`
- message -> `entry.1638878292`

Important:
- the Company field is currently appended into the message body
- if you change the connected Google Form, these field IDs will probably change

If you ever replace the Google Form:
1. get the new `formResponse` URL
2. find the new field entry IDs
3. update the `payload.append(...)` lines in the script

## Editing Success And Error Messages

At the bottom of `salesforce-admin.html`, inside the JavaScript:

- `Please fill in the required fields.`
- `Sending your message...`
- `Message sent successfully. We will get back to you soon.`

You can change that wording directly in the script.

## Editing Styles

All page-specific CSS is inside the `<style>` block in `salesforce-admin.html`.

Main style groups:
- layout and colors near the top
- top bar and logo styles
- hero styles
- card/grid styles
- form styles
- responsive styles inside media queries

If you want to change:
- colors: update the `:root` variables
- spacing: adjust section padding and card padding
- logo size: edit `.brand-mark img`
- form appearance: edit `.input`, `.select`, `.textarea`, `.submit-button`

## Routing Notes

This repo has a mix of:
- static HTML files like `about.html`
- a bundled React app inside `assets/index-D2RM8O5o.js`

Some HTML entry files rewrite the URL before the app starts.

Those fixes live in:
- `about.html`
- `services.html`
- `contact.html`
- `testimonials.html`

Those scripts exist because:
- the browser may load `/about.html`
- but the React router expects `/about`

If you remove those rewrite scripts, the app may show its internal 404 page again.

## Footer Text

Salesforce page footer:
- edit `<footer>` in `salesforce-admin.html`

Main site footer:
- edit the string inside `assets/index-D2RM8O5o.js`

Important:
- `assets/index-D2RM8O5o.js` is a built/minified file
- editing it is safe for small text changes, but it is not pleasant to maintain

## If You Want To Add Another Landing Page

The easiest way is:
1. copy `salesforce-admin.html`
2. rename it, for example `salesforce-consulting.html`
3. update SEO metadata
4. update hero copy and services
5. update the form options or messaging if needed
6. add links to it from the main site

## Before You Push Changes

Quick checklist:
- title and description still match the page
- CTA links work
- form still submits
- email is still correct
- logo path still works
- footer year is correct
- any `.html` links still resolve the way you expect on GitHub Pages

## Recommended Workflow

1. Edit `salesforce-admin.html`
2. Preview locally
3. Test the form
4. Test:
   - `Back to Bemris`
   - `Learn More About Bemris`
   - main CTA buttons
5. Commit and push

If you want, this guide can also be expanded into a full project README that documents the whole site, not just the Salesforce page.
