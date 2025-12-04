#!/usr/bin/python
# SIMPLE TEXT DISPLAY FROM TEXT FILE
# Autor : A.HALET

import serial
import json
import time
import sys
import os

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from os import path

#============================================
#            SERIAL CONFIG
#============================================

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.3)

#============================================
#            MATRIX CONFIG
#============================================
options = RGBMatrixOptions()
options.rows = 16
options.cols = 32
options.chain_length = 3
options.parallel = 1
options.brightness = 100
options.multiplexing = 4
options.show_refresh_rate = 0
options.limit_refresh_rate_hz = 180
#options.pwm_bits = 1
#options.row_address_type = 2
#options.pixel_mapper_config = "V-mapper;Rotate:-90"
options.disable_hardware_pulsing = 1
options.hardware_mapping = 'regular'
matrix = RGBMatrix(options = options)

#============================================
#            TEXT CONFIG
#============================================
offscreen_canvas = matrix.CreateFrameCanvas()
font = graphics.Font()
font.LoadFont("../fonts/9x18B.bdf")
pos = matrix.height

try:
    print("Press CTRL-C to stop.")

except KeyboardInterrupt:
    offscreen_canvas.Clear()
    matrix.Clear()
    sys.exit(0)


#============================================
#                MAIN LOOP
#============================================
while True: 
#============================================
#                  INIT
#============================================
    matrix.Clear()
    offscreen_canvas.Clear()

    pos_x=0
#    pos_y=font.height
    pos_y=10
    color_R=0
    color_G=0
    color_B=255

    print(pos_y)

#============================================
#            READ TEXT FILE
#============================================
    if(path.exists('/home/cvonselen/rpi-rgb-led-matrix/toprint.txt')):
        with open('/home/cvonselen/rpi-rgb-led-matrix/toprint.txt', 'r') as file:
            content = file.readlines()
            txt_to_print=content[0].decode('utf8')
            file.close()
    else :
        txt_to_print="Hello world"

    while True:
#============================================
#            GET TEXT FROM SERIAL
#============================================
        if ser.in_waiting >0:
            line = ser.readline().decode ('utf-8').rstrip()
            #print(line)
            try:
                jsonObj = json.loads(line)
                clock = jsonObj.get('time')
             #   txt_to_print = str(clock)
             #   print("time:", clock)
                ser.reset_input_buffer()
            except:
                print("Error")
#============================================
#            DISPLAY TEXT
#============================================
        offscreen_canvas.Clear()
        len_pic = graphics.DrawText(offscreen_canvas, font,pos_x, pos_y,graphics.Color(color_R,color_G,color_B),txt_to_print)
     #   pos -= 1
     #   if (pos + len_pic < 0):
     #       pos = offscreen_canvas.width
     #   time.sleep(0.01)
        #offscreen_canvas.Clear()
      #  time.sleep(0.05)
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
     #   time.sleep(0.5)
        #offscreen_canvas.Clear()
        
