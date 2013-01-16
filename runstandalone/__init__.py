#!/usr/bin/env python

import importlib
import os
import socket
import threading
try:
    from urllib.request import urlopen
except ImportError: # python2
    from urllib import urlopen
from wsgiref.simple_server import make_server


class DjangoRunStandAlone:
    def __init__(self, **args):
        self.wsgi = args['wsgi']
        self.ip = args.get('ip', '0.0.0.0')
        self.port = args.get('port', self.get_random_port())
        self.icon = args.get('icon', '')

        self.full_url_address = 'http://%s:%d' % (self.ip, self.port)

        self.server_thread = threading.Thread(target=self.run_server)
        self.server_thread.daemon = True

    def get_random_port(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.ip, 0))
        s.listen(0)
        port = s.getsockname()[1]
        s.close()
        return port

    def ping(self):
        try:
            urlopen(self.full_url_address)
        except:
            return False
        return True

    def run(self, ui_mode='gtk3'):
        if ui_mode == 'gtk3':
            from .guigtk import GuiGtk
            ui = GuiGtk(3, self)
        elif ui_mode == 'gtk2':
            from .guigtk import GuiGtk
            ui = GuiGtk(2, self)
        elif ui_mode == 'qt4':
            from .guiqt import GuiQt
            ui = GuiQt(self)
        else:
            raise Excpetion('Unknown ui mode selected: %s' % ui_mode)

        self.server_thread.start()

        while not self.ping():
            pass

        if os.path.exists(self.icon):
            ui.set_icon(self.icon)
        ui.run()

    def run_server(self):
        wsgi = importlib.import_module(self.wsgi)
        httpd = make_server(self.ip, self.port, wsgi.application)
        print ("Listening on port %d...." % self.port)
        httpd.serve_forever()

    def __del__(self):
        pass

