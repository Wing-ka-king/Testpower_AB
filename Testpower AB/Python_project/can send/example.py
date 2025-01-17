# !/usr/bin/env python
# coding: utf-8

"""
This example shows how sending a single message works.
"""

from __future__ import print_function

import can

def send_one():
    # this uses the default configuration (for example from the config file)
    # see http://python-can.readthedocs.io/en/latest/configuration.html
    bus = can.interface.Bus(bustype='virtual', channel='test')

    # Using specific buses works similar:
    # bus = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)
    # bus = can.interface.Bus(bustype='pcan', channel='PCAN_USBBUS1', bitrate=250000)
    # bus = can.interface.Bus(bustype='ixxat', channel=0, bitrate=250000)
    # bus = can.interface.Bus(bustype='vector', app_name='CANalyzer', channel=0,bitrate=250000)
    # ...

    msg = can.Message(arbitration_id=0xc0ffee, data=[0, 25, 0, 1, 3, 1, 4, 1], extended_id=True)

    try:
        bus.send_periodic(msg, period=2)
        print("Message sent on {}".format(bus.channel_info))
    except can.CanError:
        print("Message NOT sent")

    if __name__ == '__main__':
        send_one()
