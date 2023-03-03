#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, time

from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem

from PyQt5.uic import loadUi

from main_window_ui import Ui_MainWindow

from devices import LocalDevice, Agent



# Get the local Bluetooth device
local_device = LocalDevice()
agent = Agent()

class BtServerWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BtServerRF")
        self.setupUi(self)
        self.stop_button.setVisible(False)
        self.connectSignalsSlots()
        
        
    def re_info(self):
        info = local_device.info()

        if info[2] == 'PoweredOff':
            self.power_label.setText(' Off')
        else:
            self.power_label.setText(' On')
        
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
        item = QListWidgetItem(label)
        self.devices_list.addItem(item)
            
    def start_scan(self):
        agent.deviceDiscovered.connect(self.add_devices)
        agent.start()
        self.stop_button.setVisible(True)

    def stop_scan(self):
        agent.stop()
        self.stop_button.setVisible(False)
        

    def connectSignalsSlots(self):
        self.power_button.clicked.connect(self.dev_power)
        self.scan_button.clicked.connect(self.start_scan)






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
