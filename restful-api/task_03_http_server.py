#!/usr/bin/python3

import http.server
import json

class SimpleHandler(http.server.BaseHTTPRequestHandler):
    """
    a simple HTTP request handler
    """
    def do_GET(self):
        
        if self.path == "/data":
            self.send_response(200)
            object = {"name": "John", "age": 30, "city": "New York"}
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(object).encode('utf-8'))

        elif self.path == '/':
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")   # name, value
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            self.send_response(200)
            object = {"version": "1.0", "description": "A simple API built "
                      "with http.server"}
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(object).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Endpoint non found"}).encode('utf-8'))


PORT = 8000
server = http.server.HTTPServer(("", PORT), SimpleHandler)
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped listening")
