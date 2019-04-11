import csv
import time
from can import Message


def message_array(hex_data, start_bit=2):
    data = []
    while start_bit < len(hex_data):
        data.append(int(hex_data[start_bit:start_bit + 2], 16))
        start_bit = start_bit + 2
    return data


def signedhex(val, nbits):
    val = hex((val + (1 << nbits)) % (1 << nbits))
    return '0x' + val[2:].zfill(int(nbits / 4))


class Parser(object):
    all_headers = ['StoreNo', 'Date', 'Time', 'Millisecond', 'U-1', 'Urms-1', 'Umn-1', 'Udc-1', 'Urmn-1', 'Uac-1',
                   'Urange', 'I-1', 'Irms-1', 'Imn-1', 'Idc-1', 'Irmn-1', 'Iac-1', 'Irange', 'P-1', 'S-1', 'Q-1',
                   'PF-1', 'Phi-1', 'FreqU-1', 'FreqI-1', 'Uppeak-1', 'Umpeak-1', 'Ippeak-1', 'Impeak-1', 'Pppeak-1',
                   'Pmpeak-1', 'MATH', 'TIME', 'WP-1', 'WPp-1', 'WPm-1', 'q-1', 'qp-1', 'qm-1', 'U(k)-1-Total',
                   'I(k)-1-Total', 'P(k)-1-Total', 'Uhdf(k)-1-Total', 'Ihdf(k)-1-Total', 'Phdf(k)-1-Total', 'Uthd-1',
                   'Ithd-1', '---------', 'MeasureMode', 'DisplayMode', 'IntegrateMode', 'UpdateRate']

    def __init__(self, row_data, col_names):
        self.headers = col_names
        self.n_param = len(row_data)
        self.row_data = row_data

    def data_assign(self):

        global to_can_msg
        for i in range(self.n_param):
            if self.headers[i] == 'StoreNo':  # ID 100 byte size = 3
                to_can_msg = []
                byte_size = 3
                hex_data = '0x{0:0{1}X}'.format(int(self.row_data[i], 10), byte_size * 2)
                to_can_msg = [int(hex_data[2:4], 16), int(hex_data[5:6], 16), int(hex_data[7:8], 16)]
                print(Message(arbitration_id=100, data=to_can_msg))

            elif self.headers[i] == 'Date':  # ID 101 byte size = 4
                to_can_msg = []
                byte_size = 4
                date_play = int(self.row_data[i].replace("/", ""), 10)
                hex_data = '0x{0:0{1}X}'.format(date_play, byte_size * 2)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=101, data=to_can_msg))

            elif self.headers[i] == 'Time':  # ID 102 byte size = 4
                to_can_msg = []
                byte_size = 4
                time_play = int(self.row_data[i].replace(":", ""), 10)
                hex_data = '0x{0:0{1}X}'.format(time_play, byte_size * 2)
                to_can_msg = message_array(hex_data)
                # to_can_msg = [int(hex_data[2:4], 16), int(hex_data[4:6], 16), int(hex_data[6:8], 16)]
                print(Message(arbitration_id=102, data=to_can_msg))

            elif self.headers[i] == 'Millisecond':  # ID 103 byte size = 2
                to_can_msg = []
                byte_size = 2
                hex_data = '0x{0:0{1}X}'.format(int(self.row_data[i], 10), byte_size * 2)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=103, data=to_can_msg))

            elif self.headers[i] == 'U-1':  # ID 104 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 1000)
                # hex_data1 = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=104, data=to_can_msg))

            elif self.headers[i] == 'Urms-1':  # ID 105 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 1000)
                hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                # hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=105, data=to_can_msg))

            elif self.headers[i] == 'Umn-1':  # ID 106 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 1000)
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=106, data=to_can_msg))

            elif self.headers[i] == 'Udc-1':  # ID 107 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 1000)
                hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=107, data=to_can_msg))

            elif self.headers[i] == 'Urmn-1':  # ID 108 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 1000)
                hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                # hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=108, data=to_can_msg))

            elif self.headers[i] == 'Uac-1':  # ID 109 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 1000)
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=109, data=to_can_msg))

            elif self.headers[i] == 'Urange':  # ID 110 byte size = 4
                to_can_msg = []
                byte_size = 4
                if self.row_data[i] == 'Auto':
                    print(Message(arbitration_id=110, data=b'Auto'))
                    pass
                else:
                    self.row_data[i] = int(float(self.row_data[i]) * 10)
                    hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                    to_can_msg = message_array(hex_data)
                    print(Message(arbitration_id=110, data=to_can_msg))
                    pass

            elif self.headers[i] == 'I-1':  # ID 111 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 1000)
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=111, data=to_can_msg))

            elif self.headers[i] == 'Irms-1':  # ID 112 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 1000)
                hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=112, data=to_can_msg))

            elif self.headers[i] == 'Imn-1':  # ID 113 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 1000)
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=113, data=to_can_msg))

            elif self.headers[i] == 'Idc-1':  # ID 114 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 1000)
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=114, data=to_can_msg))

            elif self.headers[i] == 'Irmn-1':  # ID 115 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 1000)
                hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=115, data=to_can_msg))

            elif self.headers[i] == 'Iac-1':  # ID 116 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 1000)
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=116, data=to_can_msg))

            elif self.headers[i] == 'Irange':  # ID 117 byte size = 4
                to_can_msg = []
                byte_size = 4
                if self.row_data[i] == 'Auto':
                    print(Message(arbitration_id=117, data=b'Auto'))
                    pass
                else:
                    self.row_data[i] = int(float(self.row_data[i]) * 10)
                    hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                    to_can_msg = message_array(hex_data)
                    print(Message(arbitration_id=117, data=to_can_msg))
                    pass

            elif self.headers[i] == 'P-1':  # ID 118, byte size = 3
                to_can_msg = []
                byte_size = 3
                # print("{:.2f}".format(float(self.row_data[i])))
                self.row_data[i] = int(float(self.row_data[i]) * 100)  # upto 2 decimal places
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=118, data=to_can_msg))

            elif self.headers[i] == 'S-1':  # ID 119, byte size = 3
                to_can_msg = []
                byte_size = 3
                # print("{:.2f}".format(float(self.row_data[i])))
                self.row_data[i] = int(float(self.row_data[i]) * 100)  # upto 2 decimal places
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=119, data=to_can_msg))

            elif self.headers[i] == 'Q-1':  # ID 120, byte size = 3
                to_can_msg = []
                byte_size = 3
                # print("{:.2f}".format(float(self.row_data[i])))
                self.row_data[i] = int(float(self.row_data[i]) * 100)  # upto 2 decimal places
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=120, data=to_can_msg))

            elif self.headers[i] == 'PF-1':  # ID 121, byte size = 5
                to_can_msg = []
                byte_size = 5
                if self.row_data[i] == 'Error    ':
                    print(Message(arbitration_id=121, data=b'Error'))
                    pass
                else:
                    self.row_data[i] = int(float(self.row_data[i]) * 1000)
                    # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                    hex_data = signedhex(self.row_data[i], byte_size * 8)
                    to_can_msg = message_array(hex_data)
                    print(Message(arbitration_id=121, data=to_can_msg))
                    pass

            elif self.headers[i] == 'Phi-1':  # ID 122, byte size = 5
                to_can_msg = []
                byte_size = 5
                if self.row_data[i] == 'Error    ':
                    print(Message(arbitration_id=122, data=b'Error'))
                    pass
                else:
                    self.row_data[i] = int(float(self.row_data[i]) * 1000)
                    # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                    hex_data = signedhex(self.row_data[i], byte_size * 8)
                    to_can_msg = message_array(hex_data)
                    print(Message(arbitration_id=122, data=to_can_msg))
                    pass

            elif self.headers[i] == 'FreqU-1':  # ID 123, byte size = 5
                to_can_msg = []
                byte_size = 5
                if self.row_data[i] == 'Error    ':
                    print(Message(arbitration_id=123, data=b'Error'))
                else:
                    self.row_data[i] = int(float(self.row_data[i]) * 1000)
                    hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                    to_can_msg = message_array(hex_data)
                    print(Message(arbitration_id=123, data=to_can_msg))

            elif self.headers[i] == 'FreqI-1':  # ID 124, byte size = 5
                to_can_msg = []
                byte_size = 5
                if self.row_data[i] == 'Error    ':
                    print(Message(arbitration_id=124, data=b'Error'))
                    pass
                else:
                    self.row_data[i] = int(float(self.row_data[i]) * 1000)
                    hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                    to_can_msg = message_array(hex_data)
                    print(Message(arbitration_id=124, data=to_can_msg))
                    pass  # check the use of pass

            elif self.headers[i] == 'Uppeak-1':  # ID 125 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 1000)
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=125, data=to_can_msg))

            elif self.headers[i] == 'Umpeak-1':  # ID 126 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 1000)
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=126, data=to_can_msg))

            elif self.headers[i] == 'Ippeak-1':  # ID 127 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 1000)
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=127, data=to_can_msg))

            elif self.headers[i] == 'Impeak-1':  # ID 128 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 1000)
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=128, data=to_can_msg))

            elif self.headers[i] == 'Pppeak-1':  # ID 129 byte size = 4
                to_can_msg = []
                byte_size = 4
                self.row_data[i] = int(float(self.row_data[i]) * 1000)
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=129, data=to_can_msg))

            elif self.headers[i] == 'Pmpeak-1':  # ID 130 byte size = 4
                to_can_msg = []
                byte_size = 4
                self.row_data[i] = int(float(self.row_data[i]) * 1000)
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=130, data=to_can_msg))

            elif self.headers[i] == 'MATH':  # ID 131 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 10000)
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=131, data=to_can_msg))

            elif self.headers[i] == 'TIME':  # ID 132 byte size = 4
                to_can_msg = []
                byte_size = 4
                if self.row_data[i] == 'NAN':
                    print(Message(arbitration_id=132,data=[0xff, 0xff, 0xff, 0xfe]))
                    pass
                else:
                    time_play = int(float(self.row_data[i].replace(":", "")) * 1000)
                    hex_data = '0x{0:0{1}X}'.format(time_play, byte_size * 2)
                    # hex_data = signedhex(self.row_data[i], byte_size * 8)
                    to_can_msg = message_array(hex_data)
                    print(Message(arbitration_id=132, data=to_can_msg))
                    pass

            elif self.headers[i] == 'WP-1':  # ID 133 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 10E8)
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=133, data=to_can_msg))

            elif self.headers[i] == 'WPp-1':  # ID 134 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 10E8)
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=134, data=to_can_msg))

            elif self.headers[i] == 'WPm-1':  # ID 135 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 10E8)
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=135, data=to_can_msg))

            elif self.headers[i] == 'q-1':  # ID 136 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 10E6)
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=136, data=to_can_msg))

            elif self.headers[i] == 'qp-1':  # ID 135 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 10E6)
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=135, data=to_can_msg))

            elif self.headers[i] == 'qm-1':  # ID 136 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 10E6)
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=136, data=to_can_msg))

            elif self.headers[i] == 'U(k)-1-Total':  # ID 139 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 10E3)
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=139, data=to_can_msg))

            elif self.headers[i] == 'I(k)-1-Total':  # ID 140 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 10E3)
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=140, data=to_can_msg))

            elif self.headers[i] == 'P(k)-1-Total':  # ID 141 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 10E3)
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=141, data=to_can_msg))

            elif self.headers[i] == 'Uhdf(k)-1-Total':  # ID 142, byte size = 3
                to_can_msg = []
                byte_size = 3
                if self.row_data[i] == 'NAN':
                    print(Message(arbitration_id=142, data=b'NAN'))
                    pass
                else:
                    self.row_data[i] = int(float(self.row_data[i]) * 1000)
                    # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                    hex_data = signedhex(self.row_data[i], byte_size * 8)
                    to_can_msg = message_array(hex_data)
                    print(Message(arbitration_id=142, data=to_can_msg))
                    pass

            elif self.headers[i] == 'Ihdf(k)-1-Total':  # ID 143, byte size = 3
                to_can_msg = []
                byte_size = 3
                if self.row_data[i] == 'NAN':
                    print(Message(arbitration_id=143, data=b'NAN'))
                    pass
                else:
                    self.row_data[i] = int(float(self.row_data[i]) * 1000)
                    # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                    hex_data = signedhex(self.row_data[i], byte_size * 8)
                    to_can_msg = message_array(hex_data)
                    print(Message(arbitration_id=143, data=to_can_msg))
                    pass

            elif self.headers[i] == 'Phdf(k)-1-Total':  # ID 144, byte size = 3
                to_can_msg = []
                byte_size = 3
                if self.row_data[i] == 'NAN':
                    print(Message(arbitration_id=144, data=b'NAN'))
                    pass
                else:
                    self.row_data[i] = int(float(self.row_data[i]) * 1000)
                    # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                    hex_data = signedhex(self.row_data[i], byte_size * 8)
                    to_can_msg = message_array(hex_data)
                    print(Message(arbitration_id=144, data=to_can_msg))
                    pass

            elif self.headers[i] == 'Uthd-1':  # ID 145 byte size = 3
                to_can_msg = []
                byte_size = 3
                self.row_data[i] = int(float(self.row_data[i]) * 10E4)
                # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=145, data=to_can_msg))

            elif self.headers[i] == 'Ithd-1':  # ID 146 byte size = 3
                to_can_msg = []
                byte_size = 3
                if self.row_data[i]=='Error    ':
                    print(Message(arbitration_id=146, data = [0xff,0xff,0xff]))
                    pass
                else:
                    self.row_data[i] = int(float(self.row_data[i]) * 10E4)
                    # hex_data = '0x{0:0{1}X}'.format(self.row_data[i], byte_size * 2)
                    hex_data = signedhex(self.row_data[i], byte_size * 8)
                    to_can_msg = message_array(hex_data)
                    print(Message(arbitration_id=146, data=to_can_msg))
                    pass

            elif self.headers[i] == 'MeasureMode':  # ID 147 byte size = 1
                to_can_msg = []
                byte_size = 1
                hex_data = '0x{0:0{1}X}'.format(int(self.row_data[i]), byte_size * 2)
                # hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=147, data=to_can_msg))

            elif self.headers[i] == 'DisplayMode':  # ID 148 byte size = 1
                to_can_msg = []
                byte_size = 1
                hex_data = '0x{0:0{1}X}'.format(int(self.row_data[i]), byte_size * 2)
                # hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=148, data=to_can_msg))

            elif self.headers[i] == 'IntegrateMode':  # ID 149 byte size = 1
                to_can_msg = []
                byte_size = 1
                hex_data = '0x{0:0{1}X}'.format(int(self.row_data[i]), byte_size * 2)
                # hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=149, data=to_can_msg))

            elif self.headers[i] == 'UpdateRate':  # ID 150 byte size = 1
                to_can_msg = []
                byte_size = 1
                hex_data = '0x{0:0{1}X}'.format(int(self.row_data[i]), byte_size * 2)
                # hex_data = signedhex(self.row_data[i], byte_size * 8)
                to_can_msg = message_array(hex_data)
                print(Message(arbitration_id=150, data=to_can_msg))

            elif self.headers[i] == '---------':
                pass

            else:
                print(self.headers[i], self.row_data[i], "New condition encountered")
                input()

        return to_can_msg


class FileTailer(object):
    def __init__(self, file, delay=0.1):
        self.file = file
        self.delay = delay

    def __iter__(self):
        while True:
            where = self.file.tell()
            line = self.file.readline()
            if line and line.endswith('\n'):  # only emit full lines
                yield line
            else:  # for a partial line, pause and back up
                time.sleep(self.delay)  # can remove if speed getting affected
                self.file.seek(where)


csv_reader = csv.reader(FileTailer(open('myfile2.CSV')))

for row in csv_reader:
    print("Read row: %r" % (row,))
    colNames = row
    print(colNames)
    break

for row in csv_reader:
    print("Read row: %r" % (row,))
    csv_data = Parser(row, colNames)
    csv_data.data_assign()
    # break
