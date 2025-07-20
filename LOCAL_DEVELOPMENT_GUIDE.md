# Running Bemris Website Locally with Full Routing

## The Problem
Simple file servers (like Live Server or `python -m http.server`) can't handle Single Page Application (SPA) routing. When you visit `/about`, they look for an `about/index.html` file that doesn't exist.

## Solutions for Local Development

### Option 1: Python Server (Recommended)
I've created a custom Python server that handles SPA routing:

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

### Option 3: Use the Replit Development Server
Since your website was built here, you can run it locally:

```bash
# In this Replit environment
npm run dev
```

**Visit:** http://localhost:5000 (all routes work with hot reloading)

## Why Simple Servers Don't Work

**❌ Live Server/Simple HTTP Server:**
- `/` → serves `index.html` ✓
- `/about` → looks for `about/index.html` ✗ (404 error)

**✅ SPA-Aware Server:**
- `/` → serves `index.html` ✓  
- `/about` → serves `index.html` + React Router handles the route ✓

## Files Included
- `serve.py` - Python server with SPA routing
- `local-server.js` - Express server with SPA routing
- Instructions for both approaches

## Testing Your Site Locally
Once running with the proper server:
1. **Navigation works** - click About, Services, Contact, Testimonials
2. **Direct URLs work** - type `/about` in browser address bar
3. **Microinteractions work** - contact form animations function properly
4. **All features work** - exactly like it will on GitHub Pages

Your Bemris website will run perfectly locally with full routing support!