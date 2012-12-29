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
        self.webview.load(QUrl(self.dj_rsa.full_url_address))
        self.app.exec_()

    def set_icon(self, icon):
        from PyQt4.QtGui import QIcon
        self.webview.setWindowIcon(QIcon(icon))
