class GuiGtk:
    def __init__(self, version, conf):
        self.conf = conf

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
        self.scrolledwindow = Gtk.ScrolledWindow()
        self.webview = WebKit.WebView()

        self.window.add(self.scrolledwindow)
        self.scrolledwindow.add(self.webview)

        self.window.set_size_request(800, 600)
        self.window.maximize()

        self.window.connect('destroy', self._quit)

        self.webview.load_uri(self.conf['url'])
        self.webview.connect('notify::title', self.set_title)

        self.window.show_all()

    def set_title(self, webview, gtitle):
        if type(webview) == str:
            title = webview
        else:
            title = self.webview.get_title()
        if title != None:
            self.window.set_title(title)

    def run(self):
        self.Gtk.main()

    def _quit(self, window):
        self.Gtk.main_quit()

    def set_icon(self, icon):
        self.window.set_icon_from_file(icon)
