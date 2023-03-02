import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5.uic import loadUi

from main_window_ui import Ui_MainWindow

from devices import LocalDevice






class BtServerWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BtServerRF")
        self.setupUi(self)
        # self.connectSignalsSlots()
        
        # Get the local Bluetooth device
        local_device = LocalDevice()
        info = local_device.info()

        if info[2] == 0:
            self.power_label.setText(' Off')
        else:
            self.power_label.setText(' On')
        
        self.device_label.setText(f'Main local device: {info[0]} ({info[1]})')

        self.status_label.setText(f'Status: {info[2]}')
        

    #def connectSignalsSlots(self):






def main():
    if sys.platform == 'darwin':
        os.environ['QT_EVENT_DISPATCHER_CORE_FOUNDATION'] = '1'
        
    app = QApplication([])
    window = BtServerWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
