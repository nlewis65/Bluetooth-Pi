# HCCI Tool
When initially setting up the raspberry pi’s the following commands should be run through command line in the following order:
###########################################################################
Bluetoothctl

Discoverable on	#Sets device to be discoverable by other devices

Pairable on		#Sets device to be pairable

Ctrl+z		#Exits Bluetoothctl
					# commands in this section are run by both
					# RPi’s
sudo hciconfig hci0 reset	# Resets Bluetooth Adaptor 

sudo invoke-rc.d bluetooth restart	#Restart bluetooth Service

sudo hciconfig hci0 piscan	# Makes the Raspberry Pi Discoverable through
					# Host Controller Interface
##############################################################

sudo rfcomm watch hci0   # run by slave pi 

sudo rfcomm connect hci0 XX:XX:XX:XX:XX:XX  # run by master pi

hcitool rssi XX:XX:XX:XX:XX:XX

You can then run the python code to figure the distance between two devices
