from Tkinter import *
import ttk
from textwrap import wrap
import xlwt

file_name= "input_from_user"
user_path="input_path_from_user"
user_path_end = "\\"
file_type=".txt"
save_file_type=".xls"

def bind_pathname(event):
    global user_path
    user_path = path.get()
    print (user_path)

def bind_filename(event):
    global file_name
    file_name = filename.get()
    print file_name

def quit_parse(event):
    global root
    root.quit()


root = Tk()
root.title("IX UCMS LOG PARSER")
root.geometry('400x70')

Label(root,text="Path\\").grid(row=0,column=0,sticky=W)

path = Entry(root,width=40)
path.grid(row=0,column=1,sticky=W)

enterButton = Button(root,text="ENTER")
enterButton.bind("<Button-1>",bind_pathname)
enterButton.grid(row=0,column=2,sticky=W)

Label(root,text="File Name").grid(row=5,column=0,sticky=W)

filename = Entry(root,width=40)
filename.grid(row=5,column=1,sticky=W)

enterButton2 = Button(root,text="ENTER")
enterButton2.bind("<Button-1>",bind_filename)
enterButton2.grid(row=5,column=2,sticky=W)

exitButton = Button(root,text="PARSE")
exitButton.bind("<Button-1>",quit_parse)
exitButton.grid(row=5,column=3,sticky=W)

root.mainloop()

file_path=user_path+user_path_end+file_name+file_type
save_file_name=file_name + save_file_type

file=open(file_path,"r+")
l=file.read()
length = len(l)
file.close()
leng=length/264

file=open(file_path,"r+")
pos=0
pos1=0
var_check=0
var_check_1=0
var_check_2 = 0
var_check_3 = 0

crc='00000000' #inital crc byte to store final crc
crc_2 ='00000000'
poly='10010001' #0x91 poly used for crc check
poly_2= '10011011'#0x9b poly used for rev3.7

#function to convert hex to decimal
def hex_dec(val_hex_dec):
    i=int(val_hex_dec,16)
    return i

#function to convert hex to signed decimal
def sH_d16(value):
    return -(value & 0x8000) | (value & 0x7fff)

#function to tell the position of the pointer
def position():
    position = file.tell()
    return position

#define to determine the start of the string
def start_string():
    y=0;a=0;b=0;c=0
    while(a!=68 and b!=65):
        r=hex_dec(file.read(2))
        if(r==68):
            r=hex_dec(file.read(2))
            if(r==65):
                a=68
                b=65
                c=position()
    return c

pos = start_string()
pos1 = pos-4
file.close()

file=open(file_path,"r+")

for x in range(0,pos1):
    file.read(1)

wb = xlwt.Workbook()
ws = wb.add_sheet('Parsed Data')

def reset_start():
    var_a_check = 0
    var_b_check = 0
    var_c_check = 0
    var_d_check = 0

#function for LUT
def lut(count_temp_lut):
    
    if(count_temp_lut>-14351 and count_temp_lut<-14068):
        ctl_1 = count_temp_lut-(-14351)
        ctl_2 = ctl_1 * ((5.0/(-14068.0 - (-14351.0))))
        return (80 + ctl_2)

    if(count_temp_lut>-14068 and count_temp_lut<-13742):
        ctl_1 = count_temp_lut-(-14068)
        ctl_2 = ctl_1 * ((5.0/(3-13742.0 - (-14068.0))))
        return (75 + ctl_2)

    if(count_temp_lut>-13742 and count_temp_lut<-13365):
        ctl_1 = count_temp_lut-(-13742)
        ctl_2 = ctl_1 * ((5.0/(-13365.0 - (-13742.0))))
        return (70 + ctl_2)

    if(count_temp_lut>-13365 and count_temp_lut<-12929):
        ctl_1 = count_temp_lut-(-13365)
        ctl_2 = ctl_1 * ((5.0/(-12929.0 - (-13365.0))))
        return (65 + ctl_2)

    if(count_temp_lut>-12929 and count_temp_lut<-12424):
        ctl_1 = count_temp_lut-(-12929)
        ctl_2 = ctl_1 * ((5.0/(-12424.0 - (-12929.0))))
        return (60 + ctl_2)

    if(count_temp_lut>-12424 and count_temp_lut<-11843):
        ctl_1 = count_temp_lut-(-12424)
        ctl_2 = ctl_1 * ((5.0/(-11843.0 - (-12424.0))))
        return (55 + ctl_2)

    if(count_temp_lut>-11843 and count_temp_lut<-11173):
        ctl_1 = count_temp_lut-(-11843)
        ctl_2 = ctl_1 * ((5.0/(-11173.0 - (-11843.0))))
        return (50 + ctl_2)

    if(count_temp_lut>-11173 and count_temp_lut<-10404):
        ctl_1 = count_temp_lut-(-11173)
        ctl_2 = ctl_1 * ((5.0/(-10404.0 - (-11173.0))))
        return (45 + ctl_2)

    if(count_temp_lut>-10404 and count_temp_lut<-9525):
        ctl_1 = count_temp_lut-(-10404)
        ctl_2 = ctl_1 * ((5.0/(-9525.0 - (-10404.0))))
        return (40 + ctl_2)

    if(count_temp_lut>-9525 and count_temp_lut<-8527):
        ctl_1 = count_temp_lut-(-9525)
        ctl_2 = ctl_1 * ((5.0/(-8527.0 - (-9525.0))))
        return (35 + ctl_2)

    if(count_temp_lut>-8527 and count_temp_lut<-7401):
        ctl_1 = count_temp_lut-(-8527)
        ctl_2 = ctl_1 * ((5.0/(-7401.0 - (-8527.0))))
        return (30 + ctl_2)

    if(count_temp_lut>-7401 and count_temp_lut<-6144):
        ctl_1 = count_temp_lut-(-7401)
        ctl_2 = ctl_1 * (5.0/(-6144.0 - (-7401.0)))
        return (25 + ctl_2)

    if(count_temp_lut>-6144 and count_temp_lut<-4757):
        ctl_1 = count_temp_lut-(-6144)
        ctl_2 = ctl_1 * ((5.0/(-4757.0 - (-6144.0))))
        return (20 + ctl_2)

    if(count_temp_lut>-4757 and count_temp_lut<-3248):
        ctl_1 = count_temp_lut-(-4757)
        ctl_2 = ctl_1 * ((5.0/(-3248.0 - (-4757.0))))
        return (15 + ctl_2)

    if(count_temp_lut>-3248 and count_temp_lut<-1634):
        ctl_1 = count_temp_lut-(-3248)
        ctl_2 = ctl_1 * ((5.0/(-1634.0 - (-3248.0))))
        return (10 + ctl_2)

    if(count_temp_lut>-1634 and count_temp_lut<61):
        ctl_1 = count_temp_lut-(-1634)
        ctl_2 = ctl_1 * ((5.0/(61.0 - (-1634.0))))
        return (5 + ctl_2)

    if(count_temp_lut>61 and count_temp_lut<1804):
        ctl_1 = count_temp_lut-61
        ctl_2 = ctl_1 * ((5.0/(1804.0 - 61.0)))
        return (0 + ctl_2)

def crc_LUT_0x9b(r_crc):
    crctable = [0x0,0x9b,0xad,0x36,0xc1,0x5a,0x6c,0xf7,0x19,0x82,0xb4,0x2f,0xd8,0x43,0x75,0xee,0x32,0xa9,0x9f,0x4,0xf3,0x68,0x5e,0xc5,0x2b,0xb0,0x86,0x1d,0xea,0x71,0x47,0xdc,0x64,0xff,0xc9,0x52,0xa5,0x3e,0x8,0x93,0x7d,0xe6,0xd0,0x4b,0xbc,0x27,0x11,0x8a,0x56,0xcd,0xfb,0x60,0x97,0xc,0x3a,0xa1,0x4f,0xd4,0xe2,0x79,0x8e,0x15,0x23,0xb8,0xc8,0x53,0x65,0xfe,0x9,0x92,0xa4,0x3f,0xd1,0x4a,0x7c,0xe7,0x10,0x8b,0xbd,0x26,0xfa,0x61,0x57,0xcc,0x3b,0xa0,0x96,0xd,0xe3,0x78,0x4e,0xd5,0x22,0xb9,0x8f,0x14,0xac,0x37,0x1,0x9a,0x6d,0xf6,0xc0,0x5b,0xb5,0x2e,0x18,0x83,0x74,0xef,0xd9,0x42,0x9e,0x5,0x33,0xa8,0x5f,0xc4,0xf2,0x69,0x87,0x1c,0x2a,0xb1,0x46,0xdd,0xeb,0x70,0xb,0x90,0xa6,0x3d,0xca,0x51,0x67,0xfc,0x12,0x89,0xbf,0x24,0xd3,0x48,0x7e,0xe5,0x39,0xa2,0x94,0xf,0xf8,0x63,0x55,0xce,0x20,0xbb,0x8d,0x16,0xe1,0x7a,0x4c,0xd7,0x6f,0xf4,0xc2,0x59,0xae,0x35,0x3,0x98,0x76,0xed,0xdb,0x40,0xb7,0x2c,0x1a,0x81,0x5d,0xc6,0xf0,0x6b,0x9c,0x7,0x31,0xaa,0x44,0xdf,0xe9,0x72,0x85,0x1e,0x28,0xb3,0xc3,0x58,0x6e,0xf5,0x2,0x99,0xaf,0x34,0xda,0x41,0x77,0xec,0x1b,0x80,0xb6,0x2d,0xf1,0x6a,0x5c,0xc7,0x30,0xab,0x9d,0x6,0xe8,0x73,0x45,0xde,0x29,0xb2,0x84,0x1f,0xa7,0x3c,0xa,0x91,0x66,0xfd,0xcb,0x50,0xbe,0x25,0x13,0x88,0x7f,0xe4,0xd2,0x49,0x95,0xe,0x38,0xa3,0x54,0xcf,0xf9,0x62,0x8c,0x17,0x21,0xba,0x4d,0xd6,0xe0,0x7b]
    return crctable[r_crc]

#function to swap the hex byte
def swap(data):
    t=wrap(data,len(data)/2)
    a,b=wrap(t[0],len(t[0])/2)
    c,d=wrap(t[1],len(t[1])/2)
    return c+d+a+b

#function to conver hex to binary
def hex_bin(val_hex_bin):
    my_hexdata = val_hex_bin
    scale = 16 #equals to hexadecimal
    num_of_bits = 8
    val_bin = bin(int(my_hexdata, scale))[2:].zfill(num_of_bits)
    return val_bin

#function to give module voltage
def mod_vol(module_vol):
    count_Mvol = sH_d16(int(module_vol, 16))
    ModuleVoltage = ((int(count_Mvol) * float(552.189)) / (2**15)) + float(276.1)
    return ModuleVoltage

#function to give module temperature
def mod_temp(module_temp):
    count_temp = sH_d16(int(module_temp, 16))
    lut_temp=lut(count_temp)
    return lut_temp

#function to give LS Current
def LS_current(ls_cur_vref , ls_cur_vout):
    count_ls_cur_vout = sH_d16(int(ls_cur_vout, 16))
    count_ls_cur_vref = sH_d16(int(ls_cur_vref, 16))
    count_current_ls = (count_ls_cur_vout - count_ls_cur_vref)
    v_current_sensor_ls = ((int(count_current_ls) * float(3.348))/(2**15))
    adj_sensor_signal_ucms_ls = ((v_current_sensor_ls)*2)
    LS_current_fin = ( float(adj_sensor_signal_ucms_ls) / float(0.00533))
    return LS_current_fin

#function to give HS Current
def HS_current(hs_cur_vref , hs_cur_vout):
    count_hs_cur_vout = sH_d16(int(hs_cur_vout, 16))
    count_hs_cur_vref = sH_d16(int(hs_cur_vref, 16))
    count_current_hs = (count_hs_cur_vout - count_hs_cur_vref)
    v_current_sensor_hs = ((int(count_current_hs) * float(3.348))/(2**15))
    adj_sensor_signal_ucms_hs = ((v_current_sensor_hs)*2)
    HS_current_fin = ( float(adj_sensor_signal_ucms_hs) / float(0.00533))
    return HS_current_fin

#universal CRC-8 method
'''def crc8(msg,div,code='0000000'):
    msg = msg + code
    msg = list(msg)
    div = list(div)
    
    for i in range(0,len(msg)-len(code)):
        if msg[i] == '1':
            for j in range(0,len(div)):
                if(msg[i+j] == div[j]):
                    msg[i+j] = str(0)
            else:
                msg[i+j] = str(1)
            #msg[i+j] = str((int(msg[i+j])+int(div[j]))%2)
    return ''.join(msg[-len(code):])'''

def crc8_cal(msg,crc):
    crc_sep=[None]*8
    crc=list(crc)
    msg=list(msg)

    for i in range(0,len(msg)-1,2):
        numb=msg[i]+msg[i+1] #contains string
        rev_dec=hex_dec(numb) #to dec
        rev_hex=hex(rev_dec) #to hex
        rev_bin=hex_bin(rev_hex) #to bin
        rev_bin_new=list(rev_bin)
        
        for x in range(0,8):
            crc_sep[x] = str((int(rev_bin_new[x])+int(crc[x]))%2)

        rev_crc_new =''.join(crc_sep)
        rec_crc_hex = hex(int(rev_crc_new, 2))
        rec_crc_dec = hex_dec(rec_crc_hex)
        crc_trans = hex(crc_LUT_0x9b(rec_crc_dec))
        crc_f_trans = list(hex_bin(crc_trans))
        crc = crc_f_trans
    return hex(int(''.join(crc),2))

def xls_name():
    ws.write(0,0,"Module2Voltage")
    ws.write(0,1,"Module3Voltage")
    ws.write(0,2,"Module4Voltage")
    ws.write(0,3,"Module5Voltage")
    ws.write(0,4,"Module6Voltage")
    ws.write(0,5,"Module7Voltage")
    ws.write(0,6,"Module8Voltage")
    
    ws.write(0,7,"Module2Temperature")
    ws.write(0,8,"Module3Temperature")
    ws.write(0,9,"Module4Temperature")
    ws.write(0,10,"Module5Temperature")
    ws.write(0,11,"Module6Temperature")
    ws.write(0,12,"Module7Temperature")
    ws.write(0,13,"Module8Temperature")
    ws.write(0,14,"Module8voltage")
    ws.write(0,15,"LS Current")
    ws.write(0,16,"HS Current")
    ws.write(0,17,"Module8temperature")
    
    ws.write(0,18,"ADC_REC_GEN_CRC")
    ws.write(0,19,"ADC_SEN_CRC")
    
    ws.write(0,20,"OT FLAG")
    ws.write(0,21,"OV FLAG")
    ws.write(0,22,"HS_OVERCURRENT_FLAG")
    ws.write(0,23,"LS_OVERCURRENT_FLAG")    
    ws.write(0,24,"HS CON FLAG")
    ws.write(0,25,"HS FEEDBACK")
    ws.write(0,26,"LS CON FLAG")
    ws.write(0,27,"LS FEEDBACK")
    ws.write(0,28,"V12_Fan_Status")
    ws.write(0,29,"V24_Fan_Status") 
    ws.write(0,30,"DCAIR_Precharge_Status")
    ws.write(0,31,"DCAIR_Main_Status")
    ws.write(0,32,"DCAIR")
    ws.write(0,33,"DCAIR_FB")
    ws.write(0,34,"ACS_comm_status")
    ws.write(0,35,"ACS_HTA")
    ws.write(0,36,"ACD_comm_status")
    ws.write(0,37,"DRIVE_comm_status") 
    ws.write(0,38,"MOTOR_COOLING_comm_status")
    ws.write(0,39,"Ambient_Temp")
    ws.write(0,40,"SAFETY_status")
    ws.write(0,41,"SAFETY_SWITCH_count")

    
    ws.write(0,42,"RD_REC_GEN_CRC")
    ws.write(0,43,"RD_SEN_CRC")

    ws.write(0,44,"Program_mode")
    ws.write(0,45,"Engine_State")
    ws.write(0,46,"Switch_State")
    ws.write(0,47,"Error_Code")
    ws.write(0,48,"Error_Value")
    ws.write(0,49,"Mode_Timer")
    ws.write(0,50,"Motor_RPM")
    ws.write(0,51,"Motor_Voltage")
    ws.write(0,52,"Motor_Current")
    ws.write(0,53,"External_ADC")
    ws.write(0,54,"Throttle_Level")
    ws.write(0,55,"Brake_Pressure")
    ws.write(0,56,"HCU_Frequency")
    ws.write(0,57,"Bus_Current")
    ws.write(0,58,"Bus_Voltage")
    ws.write(0,59,"Internal_temp")
    ws.write(0,60,"KTY1_Temp")
    ws.write(0,61,"KTY2_Temp")
    ws.write(0,62,"Leg_A_Temp")
    ws.write(0,63,"Leg_B_Temp")
    ws.write(0,64,"Leg_C_Temp")
    ws.write(0,65,"Aux_1_Current")
    ws.write(0,66,"Aux_2_Current")
    ws.write(0,67,"Aux_3_Current")
    ws.write(0,68,"Phase_A_Voltage")
    ws.write(0,69,"Phase_B_Voltage")
    ws.write(0,70,"Phase_C_Voltage")
    
    ws.write(0,71,"HCU_REC_GEN_CRC")
    ws.write(0,72,"HCU_SEN_CRC")

    ws.write(0,73,"Isometer_Error")
    ws.write(0,74,"Isometer_Duty_Cycle")
    ws.write(0,75,"Isometer_Duty_Frequency") 
    ws.write(0,76,"Isometer_Status")

    ws.write(0,77,"Drive_Active_OS")
    ws.write(0,78,"E_Stop_OS")
    ws.write(0,79,"Motor_Pump_OS") 
    ws.write(0,80,"Motor_Fan_OS")
    ws.write(0,81,"System_OK_OS") 
    ws.write(0,82,"Ignition_IS")
    ws.write(0,83,"Emergency_IS")
    
    ws.write(0,84,"Hour")
    ws.write(0,85,"Minute")
    ws.write(0,86,"Seconds")
    ws.write(0,87,"Year")
    ws.write(0,88,"Month")
    ws.write(0,89,"Date")
    ws.write(0,90,"RTC_init")
    ws.write(0,91,"RTC_time")
    ws.write(0,92,"ISO_IO_RTC_REC_GEN_CRC")
    ws.write(0,93,"ISO_IO_RTC_SEN_CRC")

class datastr:

   def __init__(self,var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,var20,var21,var22,var23,var24,var25,var26,var27,var28,var29,var30,var31,var32,var33,var34,var35,var36,var37,var38,var39,var40,var41,var42,var43,var44,var45,var46,var47,var48,var49,var50,var51,var52,var53,var54,var55,var56,var57,var58,var59,var60,var61,var62,var63,var64,var65,var66,var67,var68,var69,var70,var71,var72,var73,var74,var75,var76,var77,var78,var79,var80,var81,var82,var83,var84,var85,var86,var87,var88,var89,var90,var91,var92,var93,var94,var95,var96,var97,var98,var99,var100,var101,var102,var103,var104,var105,var106):
       self.Constant_1=var1
       self.Constant_2=var2
       self.major_ver=var3
       self.minor_ver=var4
       self.data_length=var5
       self.Module2Voltage=var6
       self.Module3Voltage=var7
       self.Module4Voltage=var8
       self.Module5Voltage=var9
       self.Module6Voltage=var10
       self.Module7Voltage=var11
       self.Module8Voltage=var12
       self.Module2Temperature=var13
       self.Module3Temperature=var14
       self.Module4Temperature=var15
       self.Module5Temperature=var16
       self.Module6Temperature=var17
       self.Module7Temperature=var18
       self.Module8Temperature=var19
       self.Module8voltage=var20
       self.LS_Current_Vout=var21
       self.LS_Current_Vref=var22
       self.HS_Current_Vref=var23
       self.HS_Current_Vout=var24
       self.Module8temperature=var25
       self.adc_crc=var26

       self.OT_Flag=var27
       self.OV_Flag=var28
       self.HS_Overcurrent_Flag=var29
       self.LS_Overcurrent_Flag=var30
       self.HS_CON_Flag=var31
       self.HS_Feedback=var32
       self.LS_CON_Flag=var33
       self.LS_Feedback=var34
       self.V12_Fan_Status=var35
       self.V24_Fan_Status=var36
       self.DCAIR_Precharge_Status=var37
       self.DCAIR_Main_Status=var38
       self.DCAIR=var39
       self.DCAIR_FB=var40
       self.ACS_comm_status=var41
       self.ACS_HTA = var42
       self.ACD_comm_status=var43
       self.HS_comm_status=var44
       self.LS_comm_status=var45
       self.DRIVE_comm_status=var46
       self.MOTOR_COOLING_comm_status=var47
       self.Ambient_Temp=var48
       self.SAFETY_status=var49
       self.SAFETY_SWITCH_count=var50
       self.rd_crc=var51
       
       self.Program_mode=var52
       self.Engine_State=var53
       self.Switch_State=var54
       self.Error_Code=var55
       self.Error_Value=var56
       self.Mode_Timer=var57
       self.Motor_RPM=var58
       self.Motor_Current=var59
       self.Motor_Voltage=var60
       self.External_ADC=var61
       self.Throttle_Level=var62
       self.Brake_Pressure=var63
       self.HCU_Frequency=var64
       self.Bus_Current=var65
       self.Bus_Voltage=var66
       self.Internal_temp=var67
       self.KTY1_Temp=var68
       self.KTY2_Temp=var69
       self.Leg_A_Temp=var70
       self.Leg_B_Temp=var71
       self.Leg_C_Temp=var72
       self.Aux_1_Current=var73
       self.Aux_2_Current=var74
       self.Aux_3_Current=var75
       self.Phase_A_Voltage=var76
       self.Phase_B_Voltage=var77
       self.Phase_C_Voltage=var78
       self.hcu_crc=var79

       self.Isometer_Error=var80
       self.Isometer_Duty_Cycle=var81
       self.Isometer_Duty_Frequency=var82
       self.Isometer_Status=var83
       self.drive_active_os=var84
       self.E_stop_os=var85
       self.motor_pump_os=var86
       self.motor_fan_os=var87
       self.system_OK_os=var88
       self.ignition_is=var89
       self.emergency_is=var90
       self.Hour=var91
       self.Minute=var92
       self.Seconds=var93
       self.Year=var94
       self.Month=var95
       self.Date=var96
       self.RTC_init=var97
       self.RTC_time=var98
       self.Filler_6=var99
       self.iso_io_rtc_crc=var100
       
       self.END_Frame_1=var101
       self.END_Frame_2=var102
       self.Newline=var103
       self.Filler_3=var104
       self.total_crc=var105
       
       self.string_number=(var106+1)

   def displaydata(self):
       #print self.Constant_1,self.Constant_2,self.major_ver,self.minor_ver,self.data_length,self.Module2Voltage,self.Module3Voltage,self.Module4Voltage,self.Module5Voltage,self.Module6Voltage,self.Module7Voltage,self.Module8Voltage,self.Module2Temperature,self.Module3Temperature,self.Module4Temperature,self.Module5Temperature,self.Module6Temperature,self.Module7Temperature,self.Module8Temperature,self.LS_Current_Vout,self.LS_Current_Vref,self.Module8voltage,self.HS_Current_Vref,self.HS_Current_Vout,self.adc_crc,self.OT_Flag,self.OV_Flag,self.HS_Overcurrent_Flag,self.LS_Overcurrent_Flag,self.HS_CON_Flag,self.HS_Feedback,self.LS_CON_Flag,self.LS_Feedback,self.V12_Fan_Status,self.V24_Fan_Status,self.DCAIR_Precharge_Status,self.DCAIR_Main_Status,self.DCAIR,self.DCAIR_FB,self.rd_crc,self.Program_mode,self.Engine_State,self.Switch_State,self.Error_Code,self.Error_Value,self.Mode_Timer,self.Motor_RPM,self.Motor_Current,self.Motor_Voltage,self.External_ADC,self.Throttle_Level,self.Brake_Pressure,self.HCU_Frequency,self.Bus_Current,self.Bus_Voltage,self.Internal_temp,self.KTY1_Temp,self.KTY2_Temp,self.Leg_A_Temp,self.Leg_B_Temp,self.Leg_C_Temp,self.Aux_1_Current,self.Aux_2_Current,self.Aux_3_Current,self.Phase_A_Voltage,self.Phase_B_Voltage,self.Phase_C_Voltage,self.hcu_crc,self.Isometer_Error,self.Isometer_Duty_Cycle,self.Isometer_Duty_Frequency,self.Isometer_Status,self.drive_active_os,self.E_stop_os,self.motor_pump_os,self.motor_fan_os,self.system_OK_os,self.ignition_is,self.emergency_is,self.Hour,self.Minute,self.Seconds,self.Year,self.Month,self.Date,self.RTC_init,self.RTC_time,self.Filler_6,self.iso_io_rtc_crc,self.END_Frame_1,self.END_Frame_2,self.Newline,self.Filler_3,self.total_crc,self.string_number
       print sH_d16(int(self.LS_Current_Vout, 16)), sH_d16(int(self.LS_Current_Vref, 16)), sH_d16(int(self.HS_Current_Vout, 16)), sH_d16(int(self.HS_Current_Vref, 16))
   def modulevoltagetemperature(self):
       print mod_vol(self.Module2Voltage) , mod_vol(self.Module3Voltage) , mod_vol(self.Module4Voltage) , mod_vol(self.Module5Voltage) , mod_vol(self.Module6Voltage) , mod_vol(self.Module7Voltage) , mod_vol(self.Module8Voltage), mod_temp(self.Module2Temperature), mod_temp(self.Module3Temperature), mod_temp(self.Module4Temperature), mod_temp(self.Module5Temperature), mod_temp(self.Module6Temperature), mod_temp(self.Module7Temperature), mod_temp(self.Module8Temperature)

   def can_data(self):
       print self.Motor_RPM,self.Motor_Voltage,self.Motor_Current,self.Internal_temp
       print ((hex_dec(self.Motor_RPM))/10),((hex_dec(self.Motor_Voltage))/10),((hex_dec(self.Motor_Current))/10),((hex_dec(self.Internal_temp))/100)

   def check_crc8(self):
       adc_crc_msg = swap(self.Module2Voltage)+ swap(self.Module3Voltage)+ swap(self.Module4Voltage)+ swap(self.Module5Voltage)+ swap(self.Module6Voltage)+ swap(self.Module7Voltage)+ swap(self.Module8Voltage)+ swap(self.Module2Temperature)+ swap(self.Module3Temperature)+ swap(self.Module4Temperature)+ swap(self.Module5Temperature)+ swap(self.Module6Temperature)+ swap(self.Module7Temperature)+ swap(self.Module8Temperature)+ swap(self.Module8voltage)+ swap(self.LS_Current_Vout)+ swap(self.LS_Current_Vref)+ swap(self.HS_Current_Vref)+ swap(self.HS_Current_Vout)+ swap(self.Module8temperature)
       adc_crc_rec_gen = crc8_cal(adc_crc_msg,crc)
       self.adc_crc_rec_gen_final = adc_crc_rec_gen
       
       rd_crc_msg = self.OT_Flag+self.OV_Flag+self.HS_Overcurrent_Flag+self.LS_Overcurrent_Flag+self.HS_CON_Flag+self.HS_Feedback+self.LS_CON_Flag+self.LS_Feedback+self.V12_Fan_Status+self.V24_Fan_Status+self.DCAIR_Precharge_Status+self.DCAIR_Main_Status+self.DCAIR+self.DCAIR_FB+self.ACS_comm_status+self.ACS_HTA+self.ACD_comm_status+self.HS_comm_status+self.LS_comm_status+self.DRIVE_comm_status+self.MOTOR_COOLING_comm_status+swap(self.Ambient_Temp)+swap(self.SAFETY_status)+self.SAFETY_SWITCH_count
       rd_crc_rec_gen = crc8_cal(rd_crc_msg,crc)
       self.rd_crc_rec_gen_final = rd_crc_rec_gen
       
       hcu_crc_msg = swap(self.Program_mode) + swap(self.Engine_State) + swap(self.Switch_State) + swap(self.Error_Code) + swap(self.Error_Value) + swap(self.Mode_Timer) + swap(self.Motor_RPM) + swap(self.Motor_Current) + swap(self.Motor_Voltage) + swap(self.External_ADC) + swap(self.Throttle_Level) + swap(self.Brake_Pressure) + swap(self.HCU_Frequency) + swap(self.Bus_Current) + swap(self.Bus_Voltage) + swap(self.Internal_temp) + swap(self.KTY1_Temp) + swap(self.KTY2_Temp) + swap(self.Leg_A_Temp) + swap(self.Leg_B_Temp) + swap(self.Leg_C_Temp) + swap(self.Aux_1_Current) + swap(self.Aux_2_Current) + swap(self.Aux_3_Current) + swap(self.Phase_A_Voltage) + swap(self.Phase_B_Voltage) + swap(self.Phase_C_Voltage)
       hcu_crc_rec_gen = crc8_cal(hcu_crc_msg,crc)
       self.hcu_crc_rec_gen_final = hcu_crc_rec_gen
       
       iso_io_rtc_crc_msg = self.Isometer_Error + swap(self.Isometer_Duty_Cycle) + swap(self.Isometer_Duty_Frequency) + self.Isometer_Status + self.drive_active_os + self.E_stop_os + self.motor_pump_os + self.motor_fan_os + self.system_OK_os + self.ignition_is + self.emergency_is + self.Hour + self.Minute + self.Seconds + self.Year + self.Month + self.Date + self.RTC_init + self.RTC_time + self.Filler_6
       iso_io_rtc_crc_rec_gen = crc8_cal(iso_io_rtc_crc_msg,crc)
       self.iso_io_rtc_crc_rec_gen_final = iso_io_rtc_crc_rec_gen    

   def chk_cond_crc8(self):
       self.check_crc8()
       if( ((hex_dec(self.adc_crc_rec_gen_final)) == (hex_dec(self.adc_crc))) & ((hex_dec(self.rd_crc_rec_gen_final)) == (hex_dec(self.rd_crc))) & ((hex_dec(self.hcu_crc_rec_gen_final)) == (hex_dec(self.hcu_crc))) & ((hex_dec(self.iso_io_rtc_crc_rec_gen_final)) == (hex_dec(self.iso_io_rtc_crc)))):
           print "CRC_OK"

       
   def string_exp_xls(self):
       self.check_crc8()
       ws.write(self.string_number,0,mod_vol(self.Module2Voltage))
       ws.write(self.string_number,1,mod_vol(self.Module3Voltage))
       ws.write(self.string_number,2,mod_vol(self.Module4Voltage))
       ws.write(self.string_number,3,mod_vol(self.Module5Voltage))
       ws.write(self.string_number,4,mod_vol(self.Module6Voltage))
       ws.write(self.string_number,5,mod_vol(self.Module7Voltage))
       ws.write(self.string_number,6,mod_vol(self.Module8Voltage))
       ws.write(self.string_number,7,mod_temp(self.Module2Temperature))
       ws.write(self.string_number,8,mod_temp(self.Module3Temperature))
       ws.write(self.string_number,9,mod_temp(self.Module4Temperature))
       ws.write(self.string_number,10,mod_temp(self.Module5Temperature))
       ws.write(self.string_number,11,mod_temp(self.Module6Temperature))
       ws.write(self.string_number,12,mod_temp(self.Module7Temperature))
       ws.write(self.string_number,13,mod_temp(self.Module8Temperature))
       ws.write(self.string_number,14,mod_vol(self.Module8voltage))
       ws.write(self.string_number,15,LS_current(self.LS_Current_Vref,self.LS_Current_Vout))
       ws.write(self.string_number,16,HS_current(self.HS_Current_Vref,self.HS_Current_Vout))
       ws.write(self.string_number,17,mod_temp(self.Module8temperature))       

       ws.write(self.string_number,18,self.adc_crc_rec_gen_final)
       ws.write(self.string_number,19,self.adc_crc)
       
       ws.write(self.string_number,20,hex_bin(self.OT_Flag))
       ws.write(self.string_number,21,hex_bin(self.OV_Flag))
       ws.write(self.string_number,22,self.HS_Overcurrent_Flag)
       ws.write(self.string_number,23,self.LS_Overcurrent_Flag)
       ws.write(self.string_number,24,self.HS_CON_Flag)
       ws.write(self.string_number,25,self.HS_Feedback)
       ws.write(self.string_number,26,self.LS_CON_Flag)
       ws.write(self.string_number,27,self.LS_Feedback)
       ws.write(self.string_number,28,self.V12_Fan_Status)
       ws.write(self.string_number,29,self.V24_Fan_Status)
       ws.write(self.string_number,30,self.DCAIR_Precharge_Status)
       ws.write(self.string_number,31,self.DCAIR_Main_Status)
       ws.write(self.string_number,32,self.DCAIR)
       ws.write(self.string_number,33,self.DCAIR_FB)
       ws.write(self.string_number,34,self.ACS_comm_status)
       ws.write(self.string_number,35,self.ACS_HTA)
       ws.write(self.string_number,36,self.ACD_comm_status)
       ws.write(self.string_number,37,hex_dec(self.DRIVE_comm_status))
       ws.write(self.string_number,38,hex_dec(self.MOTOR_COOLING_comm_status))
       ws.write(self.string_number,39,hex_dec(self.Ambient_Temp))
       ws.write(self.string_number,40,self.SAFETY_status)
       ws.write(self.string_number,41,hex_dec(self.SAFETY_SWITCH_count))
       
       ws.write(self.string_number,42,self.rd_crc_rec_gen_final)
       ws.write(self.string_number,43,self.rd_crc)
       
       ws.write(self.string_number,44,hex_dec(self.Program_mode))
       ws.write(self.string_number,45,hex_dec(self.Engine_State))
       ws.write(self.string_number,46,hex_dec(self.Switch_State))
       ws.write(self.string_number,47,hex_dec(self.Error_Code))
       ws.write(self.string_number,48,hex_dec(self.Error_Value))
       ws.write(self.string_number,49,hex_dec(self.Mode_Timer))
       ws.write(self.string_number,50,((hex_dec(self.Motor_RPM))/10))
       ws.write(self.string_number,51,((hex_dec(self.Motor_Current))/10))
       ws.write(self.string_number,52,((hex_dec(self.Motor_Voltage))/10))
       ws.write(self.string_number,53,((hex_dec(self.External_ADC))/100))
       ws.write(self.string_number,54,((hex_dec(self.Throttle_Level))/100))
       ws.write(self.string_number,55,((hex_dec(self.Brake_Pressure))/100))
       ws.write(self.string_number,56,hex_dec(self.HCU_Frequency))
       ws.write(self.string_number,57,(sH_d16(int(self.Bus_Current, 16))/10)) #(hex_dec(self.Bus_Current))
       ws.write(self.string_number,58,((hex_dec(self.Bus_Voltage))/10))
       ws.write(self.string_number,59,((hex_dec(self.Internal_temp))/100))
       ws.write(self.string_number,60,((hex_dec(self.KTY1_Temp))/100))
       ws.write(self.string_number,61,((hex_dec(self.KTY2_Temp))/100))
       ws.write(self.string_number,62,((hex_dec(self.Leg_A_Temp))/100))
       ws.write(self.string_number,63,((hex_dec(self.Leg_B_Temp))/100))
       ws.write(self.string_number,64,((hex_dec(self.Leg_C_Temp))/100))
       ws.write(self.string_number,65,hex_dec(self.Aux_1_Current))
       ws.write(self.string_number,66,hex_dec(self.Aux_2_Current))
       ws.write(self.string_number,67,hex_dec(self.Aux_3_Current))
       ws.write(self.string_number,68,((hex_dec(self.Phase_A_Voltage))/10))
       ws.write(self.string_number,69,((hex_dec(self.Phase_B_Voltage))/10))
       ws.write(self.string_number,70,((hex_dec(self.Phase_C_Voltage))/10))

       ws.write(self.string_number,71,self.hcu_crc_rec_gen_final)
       ws.write(self.string_number,72,self.hcu_crc)

       ws.write(self.string_number,73,self.Isometer_Error)
       ws.write(self.string_number,74,hex_dec(self.Isometer_Duty_Cycle))
       ws.write(self.string_number,75,hex_dec(self.Isometer_Duty_Frequency))
       ws.write(self.string_number,76,self.Isometer_Status)
       ws.write(self.string_number,77,self.drive_active_os)
       ws.write(self.string_number,78,self.E_stop_os)
       ws.write(self.string_number,79,self.motor_pump_os)
       ws.write(self.string_number,80,self.motor_fan_os)       
       ws.write(self.string_number,81,self.system_OK_os)
       ws.write(self.string_number,82,self.ignition_is)
       ws.write(self.string_number,83,self.emergency_is)       
       ws.write(self.string_number,84,hex_dec(self.Hour))
       ws.write(self.string_number,85,hex_dec(self.Minute))
       ws.write(self.string_number,86,hex_dec(self.Seconds))
       ws.write(self.string_number,87,hex_dec(self.Year))
       ws.write(self.string_number,88,hex_dec(self.Month))
       ws.write(self.string_number,89,hex_dec(self.Date))
       ws.write(self.string_number,90,self.RTC_init)
       ws.write(self.string_number,91,self.RTC_time)

       ws.write(self.string_number,92,self.iso_io_rtc_crc_rec_gen_final)
       ws.write(self.string_number,93,self.iso_io_rtc_crc)
    
   def save_xls(self):
       wb.save(save_file_name)

   def __del__(self):
       class_name = self.__class__.__name__

xls_name()

for x in range(0,leng):

    var_a_check=0;var_b_check=0;var_c_check=0;var_d_check=0;
    while(var_a_check!=4 and var_b_check!=4 and var_c_check!=4 and var_d_check!=1):
        r=hex_dec(file.read(1))
        if(r==4):
            r=hex_dec(file.read(1))
            if(r==4):
                r=hex_dec(file.read(1))
                if(r==4):
                    r=hex_dec(file.read(1))
                    if(r==1):
                        var_a_check = 4
                        var_b_check = 4
                        var_c_check = 4
                        var_d_check = 1
       
    data1 = datastr(str(var_a_check)+str(var_b_check),str(var_c_check)+str(var_d_check),file.read(2),file.read(2),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),swap(file.read(4)),swap(file.read(4)),file.read(2),file.read(2),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),swap(file.read(4)),file.read(2),file.read(2),swap(file.read(4)),swap(file.read(4)),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),file.read(2),swap(file.read(4)),x)
    #data1.displaydata()
    #data1.modulevoltagetemperature()
    #data1.chk_cond_crc8()
    data1.string_exp_xls()
    data1.save_xls()
    #reset_start()
    del data1

print "Parsing Done"
