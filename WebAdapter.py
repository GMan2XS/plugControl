#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer


retMesg = "ERROR"

def doRequest(sock,act):
    if act == "1":
        action = "ON"
    else:
        action = "OFF"
    if sock == "A":
        sock = "ALL"
    com = "sock" + sock + action + ".py"
    execfile(com)
    return("SOCKET " + sock + " SWITCHED " + action)

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        sockoffset = self.path.index("sock") + 5
        sock = self.path[sockoffset:sockoffset+1]
        actoffset = self.path.index("act") + 4
        act = self.path[actoffset:actoffset+1]
        retMesg =doRequest(sock,act)
        print(retMesg)
        self.send_response(200)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-length", len(DUMMY_RESPONSE))
        self.end_headers()
        self.wfile.write(retMesg)

Handler = MyRequestHandler
server = SocketServer.TCPServer(('0.0.0.0', 8080), Handler)

server.serve_forever()

