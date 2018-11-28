from PyQt5.QtWidgets import *
import sys
class Dialog(QDialog):
  def slot_method(self):
    if self.button.text() == "Ok":
      self.button.setText("Sip")
    else:
      self.button.setText("Ok")
  def __init__(self):
    super(Dialog,self).__init__()
    self.button=QPushButton("Click me")
    self.button.clicked.connect(self.slot_method)
    mainLayout=QVBoxLayout()
    mainLayout.addWidget(self.button)
    self.setLayout(mainLayout)
    self.setWindowTitle("Hello, world!")
if __name__=='__main__':
  app=QApplication(sys.argv)
  dialog=Dialog()
  dialog.exec_()