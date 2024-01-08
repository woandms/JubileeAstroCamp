import http.server
import ssl

httpd = http.server.HTTPServer(
    ("", 8000), http.server.SimpleHTTPRequestHandler
)
httpd.socket = ssl.wrap_socket(
    httpd.socket,
    certfile="cert.pem",
    keyfile="key.pem",
    server_side=True,
)
httpd.serve_forever()
