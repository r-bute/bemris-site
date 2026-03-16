# Running Bemris Website Locally

## The Problem
Simple file servers do not always mirror GitHub Pages routing cleanly. This repo uses page-specific HTML files like `about.html`, while visitors see clean URLs like `/about`.

## Solutions for Local Development

### Option 1: Python Server (Recommended)
This server maps clean routes to the matching HTML files in the repo root:

```bash
# Navigate to your website folder
cd path/to/your-website-files

# Run the custom Python server
python3 serve.py
```

**Visit:**
- http://localhost:8000/ (Home)
- http://localhost:8000/about (About page)
- http://localhost:8000/services (Services page)
- http://localhost:8000/contact (Contact with microinteractions)
- http://localhost:8000/testimonials (Testimonials page)

### Option 2: Node.js/Express Server
If you have Node.js installed:

```bash
# Install express (one time only)
npm install express

# Run the server
node local-server.js
```

**Visit:** http://localhost:3000 (all routes work)

## How Routing Works Here

**✅ GitHub Pages-style preview:**
- `/` → serves `index.html`
- `/about` → serves `about.html`
- `/services` → serves `services.html`
- `/contact` → serves `contact.html`
- `/testimonials` → serves `testimonials.html`
- `/salesforce-admin` → serves `salesforce-admin.html`
- unknown routes → serve `404.html`

## Files Included
- `serve.py` - Python server for clean local routes
- `local-server.js` - Express server for clean local routes
- Instructions for both approaches

## Testing Your Site Locally
Once running with the proper server:
1. **Navigation works** - click About, Services, Contact, Testimonials
2. **Direct URLs work** - type `/about` in browser address bar
3. **404 handling works** - try a made-up URL and confirm the fallback page appears
4. **Assets load correctly** - styles, scripts, and images should render normally

These local servers now reflect the GitHub Pages structure checked into this repo.
