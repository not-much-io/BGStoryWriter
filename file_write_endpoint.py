import http.server
import socketserver
import cgi


class WriteToFileHandler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            postvars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers.getheader('content-length'))
            postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            postvars = {}

        with open("text.txt", "w+") as f:
            f.write(postvars.get("text", "didn't find it"))

PORT = 8002

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(
    ("127.0.0.1", PORT),
    Handler
)

print("serving at port", PORT)
httpd.serve_forever()
