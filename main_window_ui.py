# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/btmainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(616, 501)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.device_label = QtWidgets.QLabel(self.centralwidget)
        self.device_label.setGeometry(QtCore.QRect(20, 70, 331, 22))
        self.device_label.setObjectName("device_label")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(390, 70, 201, 21))
        self.status_label.setObjectName("status_label")
        self.power_button = QtWidgets.QPushButton(self.centralwidget)
        self.power_button.setGeometry(QtCore.QRect(20, 10, 81, 38))
        self.power_button.setObjectName("power_button")
        self.connect_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_button.setGeometry(QtCore.QRect(380, 160, 99, 38))
        self.connect_button.setObjectName("connect_button")
        self.power_label = QtWidgets.QLabel(self.centralwidget)
        self.power_label.setGeometry(QtCore.QRect(140, 10, 67, 31))
        font = QtGui.QFont()
        font.setFamily("UbuntuMono Nerd Font")
        font.setPointSize(13)
        font.setItalic(True)
        self.power_label.setFont(font)
        self.power_label.setObjectName("power_label")
        self.scan_button = QtWidgets.QPushButton(self.centralwidget)
        self.scan_button.setGeometry(QtCore.QRect(20, 110, 131, 38))
        self.scan_button.setObjectName("scan_button")
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(160, 110, 99, 38))
        self.stop_button.setObjectName("stop_button")
        self.devices_list = QtWidgets.QListWidget(self.centralwidget)
        self.devices_list.setGeometry(QtCore.QRect(20, 160, 331, 192))
        self.devices_list.setObjectName("devices_list")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 616, 34))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.device_label.setText(_translate("MainWindow", "DevName"))
        self.status_label.setText(_translate("MainWindow", "Status: "))
        self.power_button.setText(_translate("MainWindow", "Power"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.power_label.setText(_translate("MainWindow", " Off "))
        self.scan_button.setText(_translate("MainWindow", "Scan Devices"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
