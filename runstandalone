#!/usr/bin/env python

import importlib
import os
import sys
import threading

port = 8099
wsgi_module = 'project.wsgi'

project_dir = os.path.abspath(os.path.dirname(__file__))
os.chdir(project_dir)

class DjangoRunStandAlone:
    def __init__(self):
        self.th = threading.Thread(target=self._run)
        self.th.daemon = True
    def run(self):
        self.th.start()
    def _run(self):
        wsgi = importlib.import_module(wsgi_module)
        from wsgiref.simple_server import make_server
        httpd = make_server('0.0.0.0', port, wsgi.application)
        print ("Listening on port %d...." % port)
        httpd.serve_forever()
    def __del__(self):
        pass

class GuiGtk:
    def __init__(self):
        from gi.repository import Gtk
        from gi.repository import GObject
        from gi.repository import WebKit
        
        self.Gtk = Gtk
        
        GObject.threads_init()
        
        self.window = Gtk.Window(title="%s" % port)
        #self.window.set_icon_from_file()
        self.window.maximize()

        self.scrolledwindow = Gtk.ScrolledWindow()
        self.webview = WebKit.WebView()

        self.window.add(self.scrolledwindow)
        self.scrolledwindow.add(self.webview)

        self.window.connect('destroy', self.quit)
        self.window.set_size_request(800,600)
        self.window.show_all()

        self.webview.load_uri('http://127.0.0.1:%d' % port)

    def run(self):
        self.Gtk.main()

    def quit(self, window):
        self.Gtk.main_quit()

if __name__ == '__main__':
    dj = DjangoRunStandAlone()
    gui = GuiGtk()
    dj.run()
    gui.run()
