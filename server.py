from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 3001

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Backend App-Server")

server = HTTPServer(("0.0.0.0", PORT), Handler)
print("Server running on port", PORT)
server.serve_forever()
