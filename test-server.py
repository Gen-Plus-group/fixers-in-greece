#!/usr/bin/env python3
"""
Simple HTTP server for testing the Fixers in Greece website locally
"""

import http.server
import socketserver
import os
import webbrowser
from urllib.parse import unquote

PORT = 8000
HOST = "localhost"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add headers to prevent caching during development
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Expires', '0')
        super().end_headers()
    
    def log_message(self, format, *args):
        # Custom logging format
        print(f"[{self.log_date_time_string()}] {format % args}")
    
    def do_GET(self):
        # Decode URL to handle special characters
        self.path = unquote(self.path)
        
        # Handle directory requests by serving index.html
        if self.path.endswith('/'):
            self.path += 'index.html'
        
        return super().do_GET()

def start_server():
    """Start the test server"""
    # Change to the project directory
    web_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(web_dir)
    
    Handler = MyHTTPRequestHandler
    
    print(f"\n🚀 Starting Fixers in Greece Test Server...")
    print(f"📁 Serving files from: {web_dir}")
    print(f"🌐 Server URL: http://{HOST}:{PORT}")
    print(f"\n✨ Opening browser automatically...")
    print(f"📝 Press Ctrl+C to stop the server\n")
    
    # Open browser automatically
    webbrowser.open(f'http://{HOST}:{PORT}')
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Server stopped by user")
            return

if __name__ == "__main__":
    start_server()