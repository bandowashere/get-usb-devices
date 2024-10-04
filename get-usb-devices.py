# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Get USB Devices                                                             #
# v. 20241004                                                                 #
#                                                                             #
# MIT License                                                                 #
# Copyright (c) 2024 /bandowashere                                            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



# import dependencies
import wmi  # pip install wmi



# connect to WMI
wmiObject = wmi.WMI()



# get all USB devices that are currently connected or were previously connected
usbDevices = wmiObject.Win32_USBController()
usbHistory = wmiObject.Win32_USBHub()



print("-----------")
print("| DEVICES |")
print("-----------\n")



# Print information about each USB device
for device in usbDevices:
    print("Name:                      ", device.Name)
    print("Device ID:                 ", device.DeviceID)
    print("PNP Device ID:             ", device.PNPDeviceID)
    print("Caption:                   ", device.Caption)
    print("Manufacturer:              ", device.Manufacturer)
    print("Description:               ", device.Description)
    print("Creation Class Name:       ", device.CreationClassName)
    print("System Creation Class Name:", device.SystemCreationClassName)
    print("Protocol Supported:        ", device.ProtocolSupported)
    print("Config Manager Error Code: ", device.ConfigManagerErrorCode)
    print("Config Manager User Config:", device.ConfigManagerUserConfig)
    print("Status:                    ", device.Status)
    print("-----------------------------------")

# Print information about each USB device in history.
# device.Manufacture and device.ProtocolSupported are not supported for device 
# history.
for device in usbHistory:
    print("Name:                      ", device.Name)
    print("Device ID:                 ", device.DeviceID)
    print("PNP Device ID:             ", device.PNPDeviceID)
    print("Caption:                   ", device.Caption)
    print("Description:               ", device.Description)
    print("Creation Class Name:       ", device.CreationClassName)
    print("System Creation Class Name:", device.SystemCreationClassName)
    print("Config Manager Error Code: ", device.ConfigManagerErrorCode)
    print("Config Manager User Config:", device.ConfigManagerUserConfig)
    print("Status:                    ", device.Status)
    print("-----------------------------------")
print()