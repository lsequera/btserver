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
        MainWindow.resize(747, 652)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_server_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_server_button.setGeometry(QtCore.QRect(20, 370, 99, 38))
        self.start_server_button.setObjectName("start_server_button")
        self.log_text_area = QtWidgets.QScrollArea(self.centralwidget)
        self.log_text_area.setGeometry(QtCore.QRect(20, 450, 381, 101))
        self.log_text_area.setWidgetResizable(True)
        self.log_text_area.setObjectName("log_text_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 97))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.log_text = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.log_text.setGeometry(QtCore.QRect(3, 6, 371, 81))
        font = QtGui.QFont()
        font.setFamily("UbuntuMono Nerd Font")
        self.log_text.setFont(font)
        self.log_text.setObjectName("log_text")
        self.log_text_area.setWidget(self.scrollAreaWidgetContents)
        self.log_label = QtWidgets.QLabel(self.centralwidget)
        self.log_label.setGeometry(QtCore.QRect(20, 420, 101, 22))
        self.log_label.setObjectName("log_label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 10, 271, 40))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.power_button = QtWidgets.QPushButton(self.widget)
        self.power_button.setObjectName("power_button")
        self.horizontalLayout.addWidget(self.power_button)
        self.power_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("UbuntuMono Nerd Font")
        font.setPointSize(13)
        font.setItalic(True)
        self.power_label.setFont(font)
        self.power_label.setObjectName("power_label")
        self.horizontalLayout.addWidget(self.power_label)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 70, 701, 24))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.device_label = QtWidgets.QLabel(self.widget1)
        self.device_label.setObjectName("device_label")
        self.horizontalLayout_2.addWidget(self.device_label)
        self.status_label = QtWidgets.QLabel(self.widget1)
        self.status_label.setObjectName("status_label")
        self.horizontalLayout_2.addWidget(self.status_label)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(20, 110, 271, 40))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scan_button = QtWidgets.QPushButton(self.widget2)
        self.scan_button.setObjectName("scan_button")
        self.horizontalLayout_3.addWidget(self.scan_button)
        self.stop_button = QtWidgets.QPushButton(self.widget2)
        self.stop_button.setObjectName("stop_button")
        self.horizontalLayout_3.addWidget(self.stop_button)
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(20, 160, 471, 194))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.devices_list = QtWidgets.QListWidget(self.widget3)
        self.devices_list.setObjectName("devices_list")
        self.horizontalLayout_4.addWidget(self.devices_list)
        self.connect_button = QtWidgets.QPushButton(self.widget3)
        self.connect_button.setObjectName("connect_button")
        self.horizontalLayout_4.addWidget(self.connect_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 747, 34))
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
        self.start_server_button.setText(_translate("MainWindow", "Start Server"))
        self.log_label.setText(_translate("MainWindow", "Log monitor:"))
        self.power_button.setText(_translate("MainWindow", "Power"))
        self.power_label.setText(_translate("MainWindow", "??? Off "))
        self.device_label.setText(_translate("MainWindow", "DevName"))
        self.status_label.setText(_translate("MainWindow", "Status: "))
        self.scan_button.setText(_translate("MainWindow", "Scan Devices"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
