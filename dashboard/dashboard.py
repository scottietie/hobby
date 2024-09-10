#!/usr/bin/env python3

import os

from PySide2.QtWidgets import QWidget
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout

class MainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()

    self.setStyleSheet("background-color: black;")

    layout1 = QHBoxLayout()
    layout2 = QVBoxLayout()
    test1Button = QtWidgets.QPushButton("&Hello")
    test1Button.clicked.connect(self.say_hello)
    test2Button = QtWidgets.QPushButton("&Goodbye")
    test2Button.clicked.connect(self.say_goodbye)
    layout1.addLayout(layout2)
    layout2.addWidget(test1Button)
    layout2.addWidget(test2Button)

    self.widget = QWidget()
    self.widget.setLayout(layout1)
    self.setCentralWidget(self.widget)

  def say_hello(self):
    print("hello")

  def say_goodbye(self):
    print("goodbye")

if __name__ == '__main__':
  import sys

  app = QtWidgets.QApplication(sys.argv)
  mainWin = MainWindow()
  mainWin.showFullScreen()
  sys.exit(app.exec_())
