#!/usr/bin/python3
"""simple HTTP server handling basic GET request and serving JSON response
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import socketserver


class SimpleHandler(BaseHTTPRequestHandler):
    """custom HTTP request handler
    """

    def do_GET(self):

        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            data = {"name": "John", "age": 30, "city": "New York"}
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

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
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


adress = ('', 8000)
server = HTTPServer(adress, SimpleHandler)
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped listening")