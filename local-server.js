const express = require('express');
const path = require('path');
const app = express();
const port = 3000;
const rootDir = __dirname;
const routeMap = {
  '/': 'index.html',
  '/about': 'about.html',
  '/services': 'services.html',
  '/contact': 'contact.html',
  '/testimonials': 'testimonials.html',
  '/salesforce-admin': 'salesforce-admin.html',
};

// Serve static files from the repo root so local preview matches GitHub Pages output.
app.use(express.static(rootDir));

app.get(Object.keys(routeMap), (req, res) => {
  res.sendFile(path.join(rootDir, routeMap[req.path]));
});

app.get('*', (req, res) => {
  res.status(404).sendFile(path.join(rootDir, '404.html'));
});

app.listen(port, () => {
  console.log(`Bemris website running at http://localhost:${port}`);
  console.log('All routes (/, /about, /services, /contact, /testimonials) will work properly');
});
