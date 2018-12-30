#!/usr/bin/python
# -*- coding:utf-8 -*- 

import usb.util
import usb.core
import sys
#USB\VID_1C4F&PID_0051
dev =  usb.core.find(idVendor= 0x0951, idProduct= 0x16E2)
#dev =  usb.core.find(idVendor= 0x1532, idProduct= 0x0013)
if dev is None:
    raise ValueError('Device not found')
print(dev)
#cfg = dev.get_active_configuration()
command = '\xd2\x24\x00\x03\xff\xff\xff'
dev.write(0x03,command, timeout=1000)  