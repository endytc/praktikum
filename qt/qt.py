import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit,QMainWindow
from PyQt5.QtWidgets import QLabel

from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'Contoh Qt'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('Message in statusbar.')
        self.button = QPushButton('PyQt5 button', self)
        self.button.setToolTip('This is an example button')
        self.button.move(0,70)
        self.button.clicked.connect(self.on_click)

        self.textbox = QLineEdit(self)
        self.textbox.move(40, 20)
        
        self.label = QLabel(self)
        self.label.move(0,20)
        self.label.setText("Inputan: ")

        self.show()
    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
