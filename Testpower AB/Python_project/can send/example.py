# !/usr/bin/env python
# coding: utf-8

"""
This example shows how to set up different interfaces and send and receive single message.
"""

from __future__ import print_function

import can

def send_one():
    # this uses the default configuration (for example from the config file)
    # see http://python-can.readthedocs.io/en/latest/configuration.html
    # bus = can.interface.Bus(bustype='virtual', channel='test')

    # Using specific buses works similar:
    # bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)
    bus = can.interface.Bus(bustype='pcan', channel='PCAN_USBBUS1', bitrate=250000)
    # bus = can.interface.Bus(bustype='ixxat', channel=0, bitrate=250000)
    # bus = can.interface.Bus(bustype='vector', app_name='CANalyzer', channel=0,bitrate=250000)
    # ...

    msg = can.Message(arbitration_id=0xc0ffee, data=[0, 25, 0, 1, 3, 1, 4, 1], extended_id=True)
    print("I'm in here")

    try:
        bus.send(msg)
        print("Message sent on {}".format(bus.channel_info))
        print(msg)
        bus.recv(timeout=2)
    except can.CanError:
        print("Message NOT sent")

if __name__ == '__main__':
    send_one()

    print("Done with function")