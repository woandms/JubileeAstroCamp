import http.server

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path in ["/index.html", "/style.css", "/script.js"]:
            http.server.SimpleHTTPRequestHandler.do_GET(self)
        else:
            self.send_error(404, "File not found")