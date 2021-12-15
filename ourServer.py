"""
This file contains the code for the server.
Main functions:
GET: gets an account information, gets a history of transactions
PUT: puts a transaction record into an account, puts a transaction record to the main history
DELETE: delete an account
"""

from http.server import BaseHTTPRequestHandler
import time


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Our server shall be here.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
