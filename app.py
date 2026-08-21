from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>DevOps Lab Application</h1><p>Deployment successful!</p>")

server = HTTPServer(("0.0.0.0", 8080), Handler)
print("Application running on port 8080")
server.serve_forever()
