from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
hostPort = 9000

functions = [
    ["/getQR",getQR],
    ["/scannedQR",scannedQR],
    ["/clientLeft",clientLeft],
    ["/getWorlds",getWorlds],
    ["/getWorld",getWorld],
    ["/register",register],
    ["/login",login],
    ["/",None]
]


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        
        self.send_response(200)
        self.end_headers()
        functions[self.path]()


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
