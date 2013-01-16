import importlib
import socket
from threading import Thread
from wsgiref.simple_server import make_server

try:
    from urllib.request import urlopen
except ImportError: # python2
    from urllib import urlopen

class Server:
    def __init__(self, conf):
        self.conf = conf

        self.thread = Thread(target=self.serve)
        self.thread.daemon = True

    def __del__(self):
        pass

    def ping(self):
        try:
            urlopen(self.conf['url'])
        except:
            return False
        return True

    def run(self):
        self.thread.start()
    
    def serve(self):
        wsgi = importlib.import_module(self.conf['wsgi'])
        httpd = make_server(self.conf['ip'], self.conf['port'], wsgi.application)
        print ("Listening on port %d...." % self.conf['port'])
        httpd.serve_forever()

    def quit(self):
        pass

    @classmethod
    def get_random_port(self, ip):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, 0))
        s.listen(0)
        port = s.getsockname()[1]
        s.close()
        return port
