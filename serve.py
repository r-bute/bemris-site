#!/usr/bin/env python3
import http.server
import socketserver
import os
from urllib.parse import urlparse

class SPAHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_GET(self):
        # Parse the URL
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        # If requesting a specific route that doesn't exist as a file, serve index.html
        if path in ['/about', '/services', '/contact', '/testimonials'] or path.startswith('/about/') or path.startswith('/services/') or path.startswith('/contact/') or path.startswith('/testimonials/'):
            self.path = '/index.html'
        
        return super().do_GET()

PORT = 8000
web_dir = os.path.join(os.path.dirname(__file__), 'dist', 'public')
os.chdir(web_dir)

with socketserver.TCPServer(("", PORT), SPAHTTPRequestHandler) as httpd:
    print(f"Serving Bemris website at http://localhost:{PORT}")
    print("All routes will work properly:")
    print(f"  - http://localhost:{PORT}/")
    print(f"  - http://localhost:{PORT}/about")
    print(f"  - http://localhost:{PORT}/services") 
    print(f"  - http://localhost:{PORT}/contact")
    print(f"  - http://localhost:{PORT}/testimonials")
    httpd.serve_forever()