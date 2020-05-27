# https://wikidocs.net/21920

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidget, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(self.btn_clicked)

        menubar = self.menuBar()
        # menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction) 
        
        button = QPushButton('Quit', self)
        button.move(50, 50)
        button.resize(button.sizeHint())
        button.clicked.connect(self.btn_clicked)

        self.setWindowTitle('My Qt Application')
        self.setWindowIcon(QIcon('box.png'))
        # self.move(200, 200)
        # self.resize(600, 400)
        self.setGeometry(200, 200, 600, 300)
        self.show()

    def btn_clicked(self):
        sys.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
