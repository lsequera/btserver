from PyQt5.QtBluetooth import *
from PyQt5.QtCore import QVariant

class BtServer():
    def __init__(self, device) -> None:
        self.device = device
        self.name = self.device.name()
        self.address = self.device.address()

    def start_server(self) :
        if self.device.isValid():

            # Publish the service info on the local Bluetooth device
            self.device.setHostMode(QBluetoothLocalDevice.HostDiscoverable)

            # Create a Bluetooth server
            self.server = QBluetoothServer(QBluetoothServiceInfo.RfcommProtocol)
            self.server.newConnection.connect(self.handleConnection)
            result = self.server.listen(self.address)
            if not result:
                print('Can not bind server')
                return
            
            # Set the Bluetooth service name and UUID
            service_name = 'Bluetooth RF Server'
            service_uuid = QBluetoothUuid(QBluetoothUuid.SerialPort)

            service_info = QBluetoothServiceInfo()
            service_info.setServiceName(service_name)
            service_info.setServiceUuid(service_uuid)
            service_info.setServiceAvailability(1)

            service_info.registerService(self.address)
            if service_info.isRegistered():
                print('Service registered!')

            # Start the Bluetooth server
            if self.server.isListening():
                print(f'Server {service_info.serviceName()} is listening!')
            #self.server.listen(self.address)
            
        else:
            print("No local Bluetooth device found.")

    def handleConnection(self):
        clientSocket = self.server.nextPendingConnection()
        if not clientSocket:
            print('no Client Socket')
            return
        clientSocket.readyRead.connect(self.readSocket1)
        clientSocket.connected.connect(self.readSocket)
        print("New Bluetooth client connected")
        data = clientSocket.readData(10)
        print("Received data:", data)
        clientSocket.disconnected.connect(self.closeSocket)

    def readSocket1(self):
        print("Ready")

    def readSocket(self):
        print("Conected")

    def serverError(self) -> str:
        return self.server.errorString()

    def disconnectedFromBluetooth(self) -> str:
        return 'Disconnected from bluetooth'

    def receivedBluetoothMessage(self) -> str:
        while self.server.canReadLine():
            line = self.server.readLine()
            return str(line, "utf-8")