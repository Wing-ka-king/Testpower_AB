import can

# config1 = {'interface': 'virtual', 'channel': 'test'}
# # can.util.load_config(config=config1)
# a = can.util.load_file_config()
bus1 = can.interface.Bus(bustype='virtual', channel='test')
bus2 = can.interface.Bus(bustype='virtual', channel='test')

msg1 = can.Message(arbitration_id=0xabcde, data=[1, 2, 3])

bus1.send_periodic(msg1, period=2)
msg2 = bus2.recv()
for msg in bus2:
    print(msg)
# assert msg1 == msg2
