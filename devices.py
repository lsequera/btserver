#import time
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
            # Check if the local device is currently powered on and status
            modes = {0: 'PoweredOff', 1: 'Connectable', 2: 'Discoverable', 3: 'DiscoverableLimitedInquiry'}
            mode = self.hostMode()
            
            dev_info = [name, address, modes[mode]]
            return dev_info
        else:
            print("No local Bluetooth device found.")
            return ['0']
    

class Agent(QBluetoothDeviceDiscoveryAgent):
    def __init__(self):
        super().__init__()
