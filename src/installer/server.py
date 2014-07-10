#!/usr/bin/env python
from SimpleHTTPServer import SimpleHTTPRequestHandler

HOST = 'localhost'
PORT = 10470


def do_hide():
    from os.path import expanduser
    from subprocess import Popen
    path = expanduser('~/Library/Widgets/Hide Chrome.wdgt/assets/do')
    Popen([path])
    return """I tried to click the Don't button\n"""


def do_404():
    return """404 sorry\n"""


ROUTES = {
    '/hide': (200, do_hide),
    '/exit': (200, exit),
    None: (404, do_404)
}


class TuneinwithmeHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        print self.path
        if self.path == '/hide':
            self.do_the_thing(200, do_hide())
        else:
            self.do_the_thing(404, do_404())

    def do_the_thing(self, code, message):
        self.send_response(code)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(message)

    def log_message(self, format, *args):
        pass


def server():
    from BaseHTTPServer import HTTPServer

    try:
        httpd = HTTPServer((HOST, PORT), TuneinwithmeHandler)
        print "Serving app on http://%s:%s ..." % (HOST, PORT)
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    server()
