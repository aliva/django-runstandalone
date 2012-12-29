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
        self.scrolledwindow = Gtk.ScrolledWindow()
        self.webview = WebKit.WebView()

        self.window.add(self.scrolledwindow)
        self.scrolledwindow.add(self.webview)

        self.window.set_size_request(800, 600)
        self.window.maximize()

        self.window.connect('destroy', self._quit)

        self.webview.load_uri(self.dj_rsa.full_url_address)

        self.window.show_all()

    def run(self):
        self.Gtk.main()

    def _quit(self, window):
        self.Gtk.main_quit()

    def set_icon(self, icon):
        self.window.set_icon_from_file(icon)
