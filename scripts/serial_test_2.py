#!/usr/bin/python3

import serial, string

output = " "
ser = serial.Serial('/dev/ttyUSB0', 19200, 8, 'N', 1) #timeout=0.2
while True:
  print ("----")
  while output != "":
    output = ser.readline()
    print (output)
  output = " "