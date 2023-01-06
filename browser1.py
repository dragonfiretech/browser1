import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QLineEdit, QAction, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Dragon Browser')

        # Set the background color to gray
        self.setStyleSheet("background-color: gray;")

        # Create a button to exit full screen mode
        self.exit_full_screen_button = QPushButton('Exit Full Screen', self)
        self.exit_full_screen_button.clicked.connect(self.exitFullScreen)

    # Show the window in full screen mode
        self.showFullScreen()

    def exitFullScreen(self):
        self.showNormal()

        # Create the navigation bar
        self.toolbar = QToolBar()
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)

        # Add the back, forward, and refresh buttons
        self.back_button = QAction(QIcon('Desktop/python/back.png'), 'Back', self)
        self.forward_button = QAction(QIcon('Desktop/python/forward.png'), 'Forward', self)
        self.refresh_button = QAction(QIcon('Desktop/python/refresh.png'), 'Refresh', self)

        self.toolbar.addAction(self.back_button)
        self.toolbar.addAction(self.forward_button)
        self.toolbar.addAction(self.refresh_button)

        # Add the address bar
        self.address_bar = QLineEdit()
        self.toolbar.addWidget(self.address_bar)

        # Add the webview
        self.webview = QWebEngineView()
        self.webview.load(QUrl('https://www.google.com'))

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    browser = Browser()
    sys.exit(app.exec_())
