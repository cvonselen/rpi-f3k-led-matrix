
import serial
import json


ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=0.3)

while True:
    if ser.in_waiting >0:
        line = ser.readline().decode ('utf-8').rstrip()
        print(line)
        try:
            jsonObj = json.loads(line)
            rx_time = jsonObj.get('time')
            rx_timetype = jsonObj.get('timetype')
            rx_group = jsonObj.get('group')
            rx_round = jsonObj.get('round')
            rx_flight = jsonObj.get('flight')
            rx_task = jsonObj.get('task')
            print("rx_time:", rx_time)
            print("rx_timetype:", rx_timetype)
            print("rx_group:", rx_group)
            print("rx_round:", rx_round)
            print("rx_flight:", rx_flight)
            print("rx_task:", rx_task)
            ser.reset_input_buffer()
        except:
            print("Error")