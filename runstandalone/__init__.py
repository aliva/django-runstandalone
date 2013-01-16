#!/usr/bin/env python

import os

from .server import Server


class DjangoRunStandAlone:
    def __init__(self, **args):
        self.conf = {}
        self.conf['wsgi'] = args['wsgi']
        self.conf['ip'] = args.get('ip', '0.0.0.0')
        self.conf['port'] = args.get('port', Server.get_random_port(self.conf['ip']))
        self.conf['icon'] = args.get('icon', '')
        self.conf['url'] = 'http://%s:%d' % (self.conf['ip'], self.conf['port'])

        self.server = Server(self.conf)

    def run(self, ui_mode='gtk3'):
        if ui_mode == 'gtk3':
            from .guigtk import GuiGtk
            ui = GuiGtk(3, self.conf)
        elif ui_mode == 'gtk2':
            from .guigtk import GuiGtk
            ui = GuiGtk(2, self.conf)
        elif ui_mode == 'qt4':
            from .guiqt import GuiQt
            ui = GuiQt(self.conf)
        else:
            raise Excpetion('Unknown ui mode selected: %s' % ui_mode)

        self.server.run()

        while not self.server.ping():
            pass

        if os.path.exists(self.conf['icon']):
            ui.set_icon(self.conf['icon'])
        ui.run()

    def __del__(self):
        pass

