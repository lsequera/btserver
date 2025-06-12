"""
devices.py

This module provides classes for interacting with the local Bluetooth device and for discovering Bluetooth devices using PyQt5's QtBluetooth module.

Classes:
    LocalDevice: Represents the local Bluetooth device and provides information about it.
    Agent: Handles Bluetooth device discovery.
"""
#import time
from typing import List

from PyQt5.QtBluetooth import *


class LocalDevice(QBluetoothLocalDevice):
    """
    Represents the local Bluetooth device.

    Inherits from QBluetoothLocalDevice and provides a method to retrieve information about the device.
    """
    def __init__(self):
        """
        Initializes the LocalDevice object by calling the superclass constructor.
        """
        super().__init__()
        

    def info(self) -> List[str]:
        """
        Retrieves information about the local Bluetooth device.

        Returns:
            List[str]: A list containing the device name, address, and host mode as a string.
                       If no device is found, returns ['0'].
        """
        if self.isValid():
            # Get the name of the local device
            name = self.name()
            # Get the address of the local device
            address = self.address().toString()
            # Check if the local device is currently powered on and status
            modes = {0: 'PoweredOff', 1: 'Connectable', 2: 'Discoverable', 3: 'DiscoverableLimitedInquiry'}
            mode = self.hostMode()
            
            dev_info = [name, address, modes[mode]]
            return dev_info
        else:
            print("No local Bluetooth device found.")
            return ['0']
    

class Agent(QBluetoothDeviceDiscoveryAgent):
    """
    Handles Bluetooth device discovery.

    Inherits from QBluetoothDeviceDiscoveryAgent.
    """
    def __init__(self):
        """
        Initializes the Agent object by calling the superclass constructor.
        """
        super().__init__()
