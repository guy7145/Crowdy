import json
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
import time
import qrcode
from Data.entities import worlds

hostName = "0.0.0.0"
hostPort = 8080


# generate qr
def getQR(id):
    print(id)
    img = qrcode.make(json.dumps({'id': '123456'}))
    url = '{}.png'.format(id)
    img.save(url)
    print(url)
    return url


def scannedQR(params):
    pass


def clientLeft(params):
    pass


def getWorlds():
    return worlds


def getWorld(world_name):
    return json.dumps(worlds[world_name].get_services())


def register(id):
    pass


def login(id):
    pass


functions = {
    "/getQR": getQR,
    "/scannedQR": scannedQR,
    "/clientLeft": clientLeft,
    "/getWorlds": getWorlds,
    "/getWorld": getWorld,
    "/register": register,
    "/login": login,
    "/": None
}


def parse_params(params):
    if params == '':
        return dict()
    params = [p.split('=') for p in params.split('&')]
    params = {k: v for k, v in params}
    return params


class MyServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            url_parts = self.path.split('?')
            req = url_parts[0]
            params_string = url_parts[1] if len(url_parts) >= 2 else ''
            if req not in functions.keys():
                return super().do_GET()
            params = parse_params(params_string)
            self.send_response(200)
            self.end_headers()
            print(params)
            self.wfile.write(functions[req](**params).encode("utf-8"))
        except TypeError as e:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(e.__repr__().encode("utf-8"))
        return


def listen():
    print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))
    with HTTPServer((hostName, hostPort), MyServer) as server:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
    print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))


if __name__ == '__main__':
    listen()
