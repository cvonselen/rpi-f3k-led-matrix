
import serial
import json


ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)

while True:
    if ser.in_waiting >0:
        line = ()
        try: 
            line = ser.readline().decode ('utf-8').rstrip()
#           ser.reset_input_buffer()
            print(line)
        except:
            print("Error in serial")
        try:
            jsonObj = json.loads(line)
            rx_t = jsonObj.get('t')
            rx_d = jsonObj.get('d')
            rx_slot_time = jsonObj['d']['slot_time']
            rx_no_fly = jsonObj['d']['no_fly']
            rx_time_s = jsonObj['d']['time_s']
            rx_r_num = jsonObj['d']['r_num']
            rx_g_let = jsonObj['d']['g_let']
            rx_f_num = jsonObj['d']['f_num']
            rx_sect = jsonObj['d']['sect']
            rx_task_name = jsonObj['d']['task_name']
            print("rx_t:", rx_t)
            print("rx_d:", rx_d)
            print("rx_slot_time:", rx_slot_time)
            print("rx_no_fly:", rx_no_fly)
            print("rx_time_s:", rx_time_s)
            print("rx_r_num:", rx_r_num)
            print("rx_g_let:", rx_g_let)
            print("rx_f_num:", rx_f_num)
            print("rx_sect:", rx_sect)
            print("rx_task_name:", rx_task_name)
#            print("rx_round:", rx_round)
#            print("rx_flight:", rx_flight)
#            print("rx_task:", rx_task)
#            ser.reset_input_buffer()
        except:
            print("Error")