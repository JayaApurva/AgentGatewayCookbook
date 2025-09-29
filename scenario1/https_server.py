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

# Modern way to set up SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="certs/cert.pem", keyfile="certs/key.pem")

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Wrapping socket with SSL/TLS")
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    print(f"HTTPS server running on port {PORT}")
    httpd.serve_forever()