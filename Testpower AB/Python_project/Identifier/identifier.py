import csv
import time
from can import Message


def message_array(hex_data, start_bit=2):
    data = []
    while start_bit < len(hex_data):
        data.append(int(hex_data[start_bit:start_bit + 2], 16))
        start_bit = start_bit + 2
    return data


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

        for i in range(self.n_param):
            if self.headers[i] == 'StoreNo':  # ID 100 byte size = 3
                self.to_CAN_msg = []
                hex_data = '0x{0:0{1}X}'.format(int(self.row_data[i], 10), 6)
                self.to_CAN_msg = [int(hex_data[2:4], 16), int(hex_data[5:6], 16), int(hex_data[7:8], 16)]
                print(Message(arbitration_id=100, data=self.to_CAN_msg))

            elif self.headers[i] == 'Date':  # ID 101 byte size = 4
                self.to_CAN_msg = []
                date_play = int(self.row_data[i].replace("/", ""), 10)
                hex_data = '0x{0:0{1}X}'.format(date_play, 8)
                self.to_CAN_msg = message_array(hex_data)
                print(Message(arbitration_id=101, data=self.to_CAN_msg))

            elif self.headers[i] == 'Time':  # ID 102 byte size = 3
                self.to_CAN_msg = []
                time_play = int(self.row_data[i].replace(":", ""), 10)
                hex_data = '0x{0:0{1}X}'.format(time_play, 6)
                self.to_CAN_msg = message_array(hex_data)
                # self.to_CAN_msg = [int(hex_data[2:4], 16), int(hex_data[4:6], 16), int(hex_data[6:8], 16)]
                print(Message(arbitration_id=102, data=self.to_CAN_msg))

            elif self.headers[i] == 'Millisecond':  # ID 103 byte size = 2
                self.to_CAN_msg = []
                hex_data = '0x{0:0{1}X}'.format(int(self.row_data[i], 10), 4)
                self.to_CAN_msg = message_array(hex_data)
                print(Message(arbitration_id=103, data=self.to_CAN_msg))

            elif self.headers[i] == 'U-1':  # ID 104 byte size = 2
                self.to_CAN_msg = []

        return self.to_CAN_msg

    # def tally(self):
    #     self.listed_param = []
    #     for i in self.headers:
    #         for j in self.all_headers:
    #             if i == j:
    #                 self.listed_param.append(i)
    #     return self.listed_param


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


csv_reader = csv.reader(FileTailer(open('myfile.CSV')))

for row in csv_reader:
    print("Read row: %r" % (row,))
    colNames = row
    print(colNames)
    break

for row in csv_reader:
    print("Read row: %r" % (row,))
    csv_data = Parser(row, colNames)
    csv_data.data_assign()
    break
