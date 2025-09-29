import http.server
import socketserver
import json

PORT = 3005

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        print("--- HTTP Server Received a POST request! ---")
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response = {"message": "Hello from the plain HTTP MCP server!"}
        self.wfile.write(json.dumps(response).encode('utf-8'))

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"HTTP server running on port {PORT}")
    httpd.serve_forever()