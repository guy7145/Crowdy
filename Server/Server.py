import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from Data.entities import worlds
# import qrcode

hostName = "0.0.0.0"
hostPort = 8080


# generate qr
def getQR(id):
    # img = qrcode.make({'hi': 'bye'})
    # url = '{}.png'.format(id)
    # img.save(url)
    # return '/' + url
    return 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/QR_code_for_mobile_English_Wikipedia.svg/296px-QR_code_for_mobile_English_Wikipedia.svg.png'

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
    print(params)
    params = [p.split('=') for p in params.split('&')]
    params = {k: v for k, v in params}
    return params


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            url_parts = self.path.split('?')
            req = url_parts[0]
            params_string = url_parts[1] if len(url_parts) >= 2 else ''
            if req == "/favicon.ico":
                return
            params = parse_params(params_string)
            self.send_response(200)
            self.end_headers()
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
