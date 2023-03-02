from typing import List
from PyQt5.QtBluetooth import *


class LocalDevice(QBluetoothLocalDevice):
    def __init__(self):
        super().__init__()
        

    def info(self) -> List[str]:
        
        if self.isValid():
            # Get the name of the local device
            name = self.name()
            # Get the address of the local device
            address = self.address().toString()
            # Check if the local device is currently powered on
            mode = self.hostMode()
            
            dev_info = [name, address, mode]
            return dev_info
        else:
            print("No local Bluetooth device found.")
            return ['0']
    
class Agent(QBluetoothDeviceDiscoveryAgent):
    def __init__(self):
        super().__init__()

    def listdev(self) -> List[str]:
        pass
