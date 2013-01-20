class GuiQt:
    def __init__(self, conf):
        self.conf = conf

        from PyQt4 import QtCore
        from PyQt4.QtGui import QApplication
        from PyQt4.QtWebKit import QWebView

        self.app = QApplication(list())

        self.webview = QWebView()
        self.webview.setWindowState(QtCore.Qt.WindowMaximized)

        QtCore.QObject.connect(self.webview,QtCore.SIGNAL("titleChanged (const QString&)"), self.set_title)
        self.webview.show()

    def set_title(self, title):
        self.webview.setWindowTitle(title)

    def run(self):
        from PyQt4.QtCore import QUrl
        self.webview.load(QUrl(self.conf['url']))
        self.app.exec_()

    def set_icon(self, icon):
        from PyQt4.QtGui import QIcon
        self.webview.setWindowIcon(QIcon(icon))
