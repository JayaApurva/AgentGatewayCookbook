import http.server
import socketserver
import ssl
import json

PORT = 3443

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        print("--- HTTPS Server Received a POST request! ---")
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response = {"message": "Hello from the SECURE HTTPS MCP server!"}
        self.wfile.write(json.dumps(response).encode('utf-8'))

httpd = socketserver.TCPServer(("", PORT), MyHandler)
httpd.socket = ssl.wrap_socket(httpd.socket,
                              server_side=True,
                              keyfile="certs/key.pem",
                              certfile="certs/cert.pem",
                              ssl_version=ssl.PROTOCOL_TLS)

print(f"HTTPS server running on port {PORT}")
httpd.serve_forever()