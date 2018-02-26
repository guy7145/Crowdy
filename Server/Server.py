from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
hostPort = 8080

def getQR(params):
    print(params)
def scannedQR(params):
    pass
def clientLeft(params):
    pass
def getWorlds(params):
    pass
def getWorld(params):
    pass
def register(params):
    pass
def login(params):
    pass

functions = {
    "/getQR":getQR,
    "/scannedQR":scannedQR,
    "/clientLeft":clientLeft,
    "/getWorlds":getWorlds,
    "/getWorld":getWorld,
    "/register":register,
    "/login":login,
    "/":None
}

def parse_params(params):
    ans = {}
    print(params)
    for pair in params.split('&'):
        splt = pair.split('=')
        ans[splt[0]]=splt[1]
    return ans

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        req = self.path.split('?')[0]
        if(req == "/favicon.ico"): return
        params = parse_params(self.path.split('?')[1])
        self.send_response(200)
        self.end_headers()
        functions[req](params)


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
