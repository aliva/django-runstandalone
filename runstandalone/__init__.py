#!/usr/bin/env python

import os

from .server import Server


class DjangoRunStandAlone:
    def __init__(self, **args):
        self.wsgi = args['wsgi']
        self.ip = args.get('ip', '0.0.0.0')
        self.port = args.get('port', Server.get_random_port(self.ip))
        self.icon = args.get('icon', '')

        self.full_url_address = 'http://%s:%d' % (self.ip, self.port)

        conf = {
            'wsgi': self.wsgi,
            'ip': self.ip,
            'port': self.port,
            'icon': self.icon,
            'url': self.full_url_address,
        }

        self.server = Server(conf)

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

        self.server.run()

        while not self.server.ping():
            pass

        if os.path.exists(self.icon):
            ui.set_icon(self.icon)
        ui.run()

    def __del__(self):
        pass

