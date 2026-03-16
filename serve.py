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

        route_map = {
            '/': '/index.html',
            '/about': '/about.html',
            '/services': '/services.html',
            '/contact': '/contact.html',
            '/testimonials': '/testimonials.html',
            '/salesforce-admin': '/salesforce-admin.html',
        }

        # Serve the matching HTML file for clean GitHub Pages-style routes.
        if path in route_map:
            self.path = route_map[path]
        elif path.startswith('/assets/'):
            self.path = path
        elif '.' not in os.path.basename(path):
            self.path = '/404.html'
        
        return super().do_GET()

PORT = 8000
web_dir = os.path.dirname(__file__)
os.chdir(web_dir)

with socketserver.TCPServer(("", PORT), SPAHTTPRequestHandler) as httpd:
    print(f"Serving Bemris website at http://localhost:{PORT}")
    print("All routes will work properly:")
    print(f"  - http://localhost:{PORT}/")
    print(f"  - http://localhost:{PORT}/about")
    print(f"  - http://localhost:{PORT}/services") 
    print(f"  - http://localhost:{PORT}/contact")
    print(f"  - http://localhost:{PORT}/testimonials")
    print(f"  - http://localhost:{PORT}/salesforce-admin")
    httpd.serve_forever()
