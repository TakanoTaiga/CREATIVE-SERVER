import os
import sys
import urllib.parse
import html

from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from http import HTTPStatus

from urllib.parse import parse_qs, urlparse

PORT = 80

class StubHttpRequestHandler(BaseHTTPRequestHandler):
    server_version = "HTTP Stub/0.1"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_GET(self):
        print('path = {}'.format(self.path))
        parsed_path = urlparse(self.path)
        print('parsed: path = {}, query = {}'.format(parsed_path.path, parse_qs(parsed_path.query)["hoge"]))
        self.send_response(200)
        self.send_header("User-Agent","test1")
        self.end_headers()
        html = "abc" # Here write debug data.
        self.wfile.write(html.encode())

handler = StubHttpRequestHandler
httpd = HTTPServer(('',PORT),handler)
httpd.serve_forever()