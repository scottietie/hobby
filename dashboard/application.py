#!/usr/bin/env python3

import os
import subprocess
import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtCore import QDateTime

class MainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super(MainWindow, self).__init__()

    self.old_time = ""
    self.setCursor(Qt.BlankCursor)

    self.datetime_timer = QTimer(self)
    self.datetime_timer.timeout.connect(self.refresh_datetime)
    self.datetime_timer.start(100)

    self.setStyleSheet("background-color: black;")

    layout1 = QVBoxLayout()
    layout2 = QHBoxLayout()

    self.clock = QLabel(self)
    self.date = QLabel(self)
    self.second = QLabel(self)

    self.clock.setStyleSheet('''
      font-size:120px;
      font-weight:bold;
	  font-family: Arial;
      color:lime;
            ''')
    self.clock.setAlignment(Qt.AlignCenter)

    self.date.setStyleSheet('''
      font-size:100px;
      font-weight:bold;
	  font-family: Arial;
      color:lime;
            ''')

    self.second.setStyleSheet('''
      font-size:60px;
      font-weight:bold;
	  font-family: Arial;
      color:lime;
            ''')

    self.date.setAlignment(Qt.AlignRight)

    layout1.addWidget(self.clock)
    layout2.addWidget(self.second)
    layout2.addWidget(self.date)
    layout1.addLayout(layout2)

    # layout1.addWidget(self.date)

    self.widget = QWidget()
    self.widget.setLayout(layout1)
    self.setCentralWidget(self.widget)

  def refresh_datetime(self):
    now = QDateTime.currentDateTime()

    current_second = str(now.time().second()).zfill(2)
    if self.old_time != current_second:
      self.old_time = current_second
      self.second.setText(current_second)

      current_time = str(now.time().hour())+':'+str(now.time().minute()).zfill(2)
      self.clock.setText(current_time)

      current_date = str(now.date().month())+'/'+str(now.date().day())
      self.date.setText(current_date)


if __name__ == '__main__':
  os.system('tvservice  -o')
  os.system('DISPLAY=:0 xset s off -dpms')

  app = QtWidgets.QApplication(sys.argv)
  mainWin = MainWindow()
  mainWin.setFixedSize(320, 240)
  # mainWin.show()
  mainWin.showFullScreen()
  sys.exit(app.exec_())
