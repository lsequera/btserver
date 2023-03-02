
## BtRF

This is a little project to provide bluetooth RF comunication and use it as external input for a linux distibution ...


You will need to install the development package for bluez before you run this app:

libbluetooth-dev (if you are using a distribution debian/ubuntu like).


"qt.bluetooth.bluez: Missing CAP_NET_ADMIN permission. Cannot determine whether a found address is of random or public type."

/etc/dbus-1/system.d/bluetooth.conf

`gpasswd -a <username> bluetooth`
