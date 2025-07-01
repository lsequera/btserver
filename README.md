
## BtRF

This is a little project to provide bluetooth RF comunication and use it as external input for a linux distibution ...


## Prerequisites

### Bluetooth Permissions

To use Bluetooth functionality, you'll need to:

1. Install the required development package:
   ```bash
   sudo apt-get install libbluetooth-dev
   ```

2. Add your user to the bluetooth group:
   ```bash
   sudo gpasswd -a <username> bluetooth
   ```

3. Ensure proper Bluetooth permissions in the D-Bus configuration:
   ```bash
   sudo nano /etc/dbus-1/system.d/bluetooth.conf
   ```
   Add the following lines inside the `<busconfig>` tag:
   ```xml
   <policy user="<username>">
       <allow send_destination="org.bluez"/>
       <allow send_interface="org.bluez.Agent1"/>
   </policy>
   ```

### Input Device Permissions

To enable mouse control functionality, you need to configure proper permissions for the uinput device. This is required because the program uses uinput to create virtual input devices.

1. Create a udev rule file:
   ```bash
   sudo nano /etc/udev/rules.d/99-uinput.rules
   ```
   Add the following content:
   ```
   KERNEL=="uinput", MODE="0666"
   ```

2. Load the uinput module:
   ```bash
   sudo modprobe uinput
   ```

3. Add uinput to modules to load at boot:
   ```bash
   echo "uinput" | sudo tee -a /etc/modules
   ```

4. Reload udev rules:
   ```bash
   sudo udevadm control --reload-rules
   sudo udevadm trigger
   ```

Note: The uinput device is typically located at `/dev/uinput`. The mode "0666" allows all users to read and write to the device. If you prefer to restrict access, you can modify the permissions to be more specific (e.g., "0660" for group access only).
