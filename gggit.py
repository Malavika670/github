import http.server
import socketserver

# Define the port number on which the server will listen
PORT = 8000

# Create a request handler that serves the index.html file
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'ggit.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Set up the server
with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Serving on port {PORT}. Access the website at http://localhost:{PORT}")
    httpd.serve_forever()
