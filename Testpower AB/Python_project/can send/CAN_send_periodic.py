import can

bus1 = can.interface.Bus(bustype='virtual', channel='test')
bus2 = can.interface.Bus(bustype='virtual', channel='test')

msg1 = can.Message(arbitration_id=0xabcde, data=[1, 2, 3])

bus1.send_periodic(msg1, period=2)
print("Message sent on {}".format(bus1.channel_info))
# msg2 = bus2.recv()
# for msg in bus2:        # requires for loop. bus2.recv() does not appear to work
#     print(msg)          # msg and msg2 have same data, only different timestamps