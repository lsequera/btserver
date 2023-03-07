#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, time

from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PyQt5 import QtCore
from PyQt5.QtBluetooth  import QBluetoothAddress

from main_window_ui import Ui_MainWindow

from devices import LocalDevice, Agent
from btserver import BtServer


# Get the local Bluetooth device
local_device = LocalDevice()
agent = Agent()

bt_server = BtServer(local_device)

class BtServerWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BtServerRF")
        self.setupUi(self)
        self.stop_button.setVisible(False)
        self.re_info()
        self.connectSignalsSlots()
        
        
    def re_info(self):
        info = local_device.info()

        if info[2] == 'PoweredOff':
            self.power_label.setText(' Off')
            self.power_label.setStyleSheet('QLabel { color : #ff0000}')
        else:
            self.power_label.setText(' On')
            self.power_label.setStyleSheet('QLabel { color : #84c100}')
        
        self.device_label.setText(f'Main local device: {info[0]} ({info[1]})')
        self.status_label.setText(f'Status: {info[2]}')
        
        
    def dev_power(self):
        if local_device.info()[2] == 'PoweredOff':
            local_device.powerOn()
            time.sleep(0.2)
            self.re_info()
        else:
            local_device.setHostMode(0)
            self.re_info()
            
    def add_devices(self, info):
        label = f'{info.name()} ({info.address().toString()})'
        items = self.devices_list.findItems(label, QtCore.Qt.MatchExactly)
        if len(items) == 0:
            item = QListWidgetItem(label)
            self.devices_list.addItem(item)

    def item_activated(self, item):
        text = item.text()
        tx = text.split('(')
        address = QBluetoothAddress(tx[1][:-1])
        name =  tx[0][:-1]
        print(name, address.toString(), sep=' -> ')
            
    def start_scan(self):
        agent.deviceDiscovered.connect(self.add_devices)
        agent.start()
        self.stop_button.setVisible(True)

    def stop_scan(self):
        agent.stop()
        self.stop_button.setVisible(False)

    def scan_finished(self):
        self.stop_button.setVisible(False)

    def start_server(self):
        self.server = bt_server.start_server()
        self.re_info()
        self.log_text.insertPlainText("Service started!\n")
        self.server.newConnection.connect(self.connection)
        
    def connection(self):
        self.client_socket = self.server.nextPendingConnection()
        self.client_socket.readyRead.connect(self.show_message)

    def show_message(self):
        while self.client_socket.canReadLine():
            msg = self.client_socket.read(10)
            self.log_text.insertPlainText(str(msg, 'utf-8'))

    def connectSignalsSlots(self):
        self.power_button.clicked.connect(self.dev_power)
        self.scan_button.clicked.connect(self.start_scan)
        self.stop_button.clicked.connect(self.stop_scan)
        self.devices_list.itemClicked.connect(self.item_activated)
        self.start_server_button.clicked.connect(self.start_server)
        
        agent.finished.connect(self.scan_finished)
        




def main():
    if sys.platform == 'darwin':
        os.environ['QT_EVENT_DISPATCHER_CORE_FOUNDATION'] = '1'
        
    app = QApplication([])
    #app.setStyle('QtCurve')
    window = BtServerWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
