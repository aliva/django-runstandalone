#!/usr/bin/env python

import importlib
import os
import socket
import threading
from wsgiref.simple_server import make_server

class GuiGtk:
    def __init__(self, version, dj_rsa):
        self.dj_rsa = dj_rsa

        if version == 3:
            from gi.repository import Gtk
            from gi.repository import GObject
            from gi.repository import WebKit
        elif version == 2:
            import gtk as Gtk
            import gobject as GObject
            import webkit as WebKit

        self.Gtk = Gtk
        GObject.threads_init()

        self.window = Gtk.Window()
        self.window.set_title('%d' % self.dj_rsa.port)

        self.window.maximize()

        self.scrolledwindow = Gtk.ScrolledWindow()
        self.webview = WebKit.WebView()

        self.window.add(self.scrolledwindow)
        self.scrolledwindow.add(self.webview)

        self.window.connect('destroy', self.quit)
        self.window.set_size_request(800, 600)
        self.window.show_all()

        self.webview.load_uri('http://%s:%d' % (self.dj_rsa.ip, self.dj_rsa.port))

    def run(self):
        self.Gtk.main()

    def quit(self, window):
        self.Gtk.main_quit()

    def set_icon(self, icon):
        self.window.set_icon_from_file(icon)

class GuiQt:
    def __init__(self, dj_rsa):
        self.dj_rsa = dj_rsa

        from PyQt4.QtGui import QApplication
        from PyQt4.QtCore import Qt
        from PyQt4.QtWebKit import QWebView

        self.app = QApplication(list())

        self.webview = QWebView()
        self.webview.setWindowState(Qt.WindowMaximized)

        self.webview.show()

    def run(self):
        from PyQt4.QtCore import QUrl
        self.webview.load(QUrl('http://%s:%d' % (self.dj_rsa.ip, self.dj_rsa.port)))
        self.app.exec_()

    def set_icon(self, icon):
        from PyQt4.QtGui import QIcon
        self.webview.setWindowIcon(QIcon(icon))

class DjangoRunStandAlone:
    def __init__(self, **args):
        self.wsgi = args['wsgi']
        self.ip = args.get('ip', '0.0.0.0')
        self.port = args.get('port', self.get_random_port())
        self.icon = args.get('icon', '')

        self.server_thread = threading.Thread(target=self._run_server)
        self.server_thread.daemon = True

    def get_random_port(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.ip, 0))
        s.listen(0)
        port = s.getsockname()[1]
        s.close()
        return port

    def run(self, ui_mode='gtk3'):
        if ui_mode == 'gtk3':
            ui = GuiGtk(3, self)
        elif ui_mode == 'gtk2':
            ui = GuiGtk(2, self)
        elif ui_mode == 'qt4':
            ui = GuiQt(self)
        else:
            raise Excpetion('Unknown ui mode selected: %s' % ui_mode)

        self.server_thread.start()

        if os.path.exists(self.icon):
            ui.set_icon(self.icon)
        ui.run()

    def _run_server(self):
        wsgi = importlib.import_module(self.wsgi)
        httpd = make_server(self.ip, self.port, wsgi.application)
        print ("Listening on port %d...." % self.port)
        httpd.serve_forever()

    def __del__(self):
        pass

