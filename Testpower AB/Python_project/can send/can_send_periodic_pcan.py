import can
import time
import logging

logging.basicConfig(level=logging.INFO)
def simple_periodic_send(bus):
    print("Starting to send a message every 200ms for 2s")
    msg = can.Message(arbitration_id=0x123, data=[5], extended_id=False)
    task = bus.send_periodic(msg,period=.20, duration=10)
    assert isinstance(task, can.CyclicSendTaskABC)
    time.sleep(60)
    task.stop()
    print("stopped cyclic send")


bus1 = can.interface.Bus(bustype='pcan', channel='PCAN_USBBUS1')
simple_periodic_send(bus1)
bus1.shutdown()
