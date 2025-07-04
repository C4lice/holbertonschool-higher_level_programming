#!/usr/bin/python3

'''
This module provides a simple HTTP request handler class.
'''

import http.server
import json

PORT = 8000


class Server(http.server.BaseHTTPRequestHandler):
    '''
    This class includes basic components for a HTTP server
    '''

    def do_GET(self):
        '''
        Handles GET requests.
        '''
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write('Hello, this is a simple API!'.encode("utf-8"))

        elif self.path == "/data":
            data = {"name": "John","age": 30,"city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(info).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

if __name__ == "__main__":
    with http.server.HTTPServer(("", PORT), Server) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
