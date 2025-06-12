#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
BtServerRF Main Script
---------------------
This script provides a PyQt5 GUI for managing a Bluetooth server using the local Bluetooth device.
It allows users to power the device on/off, scan for nearby devices, and start a Bluetooth server to accept connections.
"""

import sys, time

from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PyQt5 import QtCore
from PyQt5.QtBluetooth  import QBluetoothAddress
from PyQt5.QtBluetooth import QBluetoothLocalDevice

from main_window_ui import Ui_MainWindow

from devices import LocalDevice, Agent
from btserver import BtServer


# Get the local Bluetooth device
local_device = LocalDevice()
agent = Agent()

bt_server = BtServer(local_device)

class BtServerWindow(QMainWindow, Ui_MainWindow):
    """
    Main window for the BtServerRF application.
    Handles UI logic for Bluetooth device management, scanning, and server operations.
    """
    def __init__(self):
        """
        Initialize the main window, set up UI, and connect signals/slots.
        """
        super().__init__()
        self.setWindowTitle("BtServerRF")
        self.setupUi(self)
        self.stop_button.setVisible(False)
        self.re_info()
        self.connectSignalsSlots()
        
        local_device.pairingFinished.connect(self.on_pairing_finished)
        
    def re_info(self):
        """
        Refresh and display the local Bluetooth device's information (name, address, power status).
        """
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
        """
        Toggle the power state of the local Bluetooth device.
        Powers on if off, otherwise sets host mode to off.
        """
        if local_device.info()[2] == 'PoweredOff':
            local_device.powerOn()
            time.sleep(0.2)
            self.re_info()
        else:
            local_device.setHostMode(0)
            self.re_info()
            
    def add_devices(self, info):
        """
        Add a discovered Bluetooth device to the device list in the UI if not already present.
        Args:
            info: The Bluetooth device information object (with name and address).
        """
        label = f'{info.name()} ({info.address().toString()})'
        items = self.devices_list.findItems(label, QtCore.Qt.MatchExactly)
        if len(items) == 0:
            item = QListWidgetItem(label)
            self.devices_list.addItem(item)

    def item_activated(self, item):
        """
        Handle activation (click) of a device in the list. Prints the device name and address.
        Args:
            item: The QListWidgetItem that was activated.
        """
        text = item.text()
        tx = text.split('(')
        address = QBluetoothAddress(tx[1][:-1])
        name =  tx[0][:-1]
        print(name, address.toString(), sep=' -> ')
            
    def start_scan(self):
        """
        Start scanning for nearby Bluetooth devices and show the stop button.
        """
        agent.deviceDiscovered.connect(self.add_devices)
        agent.start()
        self.stop_button.setVisible(True)

    def stop_scan(self):
        """
        Stop scanning for Bluetooth devices and hide the stop button.
        """
        agent.stop()
        self.stop_button.setVisible(False)

    def scan_finished(self):
        """
        Slot called when device scanning is finished. Hides the stop button.
        """
        self.stop_button.setVisible(False)

    def start_server(self):
        """
        Start the Bluetooth server and update the UI/log.
        """
        self.server = bt_server.start_server()
        self.re_info()
        self.log_text.insertPlainText("Service started!\n")
        self.server.newConnection.connect(self.connection)
        self.update_server_status()
        
    def connection(self):
        """
        Handle a new client connection to the Bluetooth server.
        """
        self.client_socket = self.server.nextPendingConnection()
        self.client_socket.readyRead.connect(self.show_message)

    def show_message(self):
        """
        Read and display messages from the connected Bluetooth client.
        """
        while self.client_socket.canReadLine():
            msg = self.client_socket.read(10)
            self.log_text.insertPlainText(str(msg, 'utf-8'))

    def on_pairing_finished(self, address, pairing):
        """
        Handle Bluetooth device pairing status changes.
        Args:
            address: QBluetoothAddress of the device.
            pairing: QBluetoothLocalDevice.Pairing status.
        """
        # Use the enum values for clarity
        if pairing == QBluetoothLocalDevice.Unpaired:
            status_str = "Unpaired"
        elif pairing == QBluetoothLocalDevice.Paired:
            status_str = "Paired"
        elif pairing == QBluetoothLocalDevice.AuthorizedPaired:
            status_str = "Authorized Paired"
        else:
            status_str = str(pairing)
        msg = f"Pairing status changed: {address.toString()} -> {status_str}\n"
        self.log_text.insertPlainText(msg)
        self.pair_status.setText(f"Pairing Status: {status_str}")

    def update_server_status(self):
        """
        Update the server_status label based on the server's running state.
        """
        if hasattr(self, 'server') and self.server and self.server.isListening():
            self.server_status.setText("Server status: Active")
        else:
            self.server_status.setText("Server status: Inactive")

    def connectSignalsSlots(self):
        """
        Connect UI buttons and agent signals to their respective slots.
        """
        self.power_button.clicked.connect(self.dev_power)
        self.scan_button.clicked.connect(self.start_scan)
        self.stop_button.clicked.connect(self.stop_scan)
        self.devices_list.itemClicked.connect(self.item_activated)
        self.start_server_button.clicked.connect(self.start_server)
        
        agent.finished.connect(self.scan_finished)
        

def main():
    """
    Entry point for the application. Initializes and runs the Qt event loop.
    """
    if sys.platform == 'darwin':
        os.environ['QT_EVENT_DISPATCHER_CORE_FOUNDATION'] = '1'
        
    app = QApplication([])
    #app.setStyle('QtCurve')
    window = BtServerWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
