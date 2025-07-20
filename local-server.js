const express = require('express');
const path = require('path');
const app = express();
const port = 3000;

// Serve static files from dist/public directory
app.use(express.static(path.join(__dirname, 'dist/public')));

// Handle React Router - send all requests to index.html
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, 'dist/public', 'index.html'));
});

app.listen(port, () => {
  console.log(`Bemris website running at http://localhost:${port}`);
  console.log('All routes (/, /about, /services, /contact, /testimonials) will work properly');
});