from PyQt5.QtBluetooth import *
from PyQt5.QtCore import QObject
class BtServer(QObject):
    def __init__(self, device, parent=None) -> None:
        super().__init__(parent)
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
        self.clientSocket = self.server.nextPendingConnection()
        if not self.clientSocket:
            print('no Client Socket')
            return
        self.clientSocket.readyRead.connect(self.receivedMessage)
        self.clientSocket.connected.connect(self.isConnected)
        print("New Bluetooth client connected")
        
        self.clientSocket.disconnected.connect(self.closeSocket)

    def isConnected(self):
        print("Conected")
        self.clientSocket.write('Connected'.encode())

    def serverError(self) -> str:
        return self.server.errorString()

    def receivedMessage(self) -> str:
        while self.clientSocket.canReadLine():
            data = self.clientSocket.readLine(10)
            print(str(data, "utf-8"))

    def closeSocket(self) -> str:
        return 'Disconnected from bluetooth'