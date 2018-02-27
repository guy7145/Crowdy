import json
import urllib
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
import time

import os
import qrcode
from Data.entities import worlds

hostName = "0.0.0.0"
hostPort = 8080


# generate qr
def getQR(id):
    print('getQR ({})'.format(id))
    img = qrcode.make(json.dumps({'id': id, 'creation_date': time.time()}))
    url = '{}.png'.format(id)
    img.save(url)
    print(url)
    return url


def scannedQR(id, creation_date):
    print('scannedQR ({}, {})'.format(id, creation_date))
    os.remove('{}.png'.format(id))
    return 'scanned successfully'


def clientLeft(params):
    pass


def getWorlds():
    print('getWorlds')
    return str([w.get_name() for w in worlds.values()])


def getWorld(id):
    print('getWorld ({})'.format(id))
    services = list(worlds[id].get_services().values())
    ser = [json.dumps(s.__dict__()) for s in services]
    return str(ser)


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
            print(self.path)
            print(urllib.parse.unquote(self.path))
            url_parts = urllib.parse.unquote(self.path).split('?')
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
            print(e)
            self.send_response(401)
            self.end_headers()
            self.wfile.write(e.__repr__().encode("utf-8"))
        except Exception as e:
            print(e)
            self.send_response(400)
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
