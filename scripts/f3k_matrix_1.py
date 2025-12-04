#!/usr/bin/python
# SIMPLE TEXT DISPLAY FROM TEXT FILE
# Autor : A.HALET


import time
import sys
import os
import serial
import json

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from os import path

#============================================
#            SERIAL INTERFACE
#============================================

ser = serial.Serial('/dev/ttyUSB0', 19200, timeout=0.3)
#============================================
#            MATRIX CONFIG
#============================================
options = RGBMatrixOptions()
options.rows = 16
options.cols = 32
options.chain_length = 3
options.parallel = 3
options.brightness = 100
options.multiplexing = 5
options.gpio_slowdown = 3
options.show_refresh_rate = 1
options.limit_refresh_rate_hz = 1800
options.row_address_type = 2
options.pwm_lsb_nanoseconds = 120
#options.pixel_mapper_config = "V-mapper;Rotate:-90"
#options.disable_hardware_pulsing = 1
options.pwm_bits = 1
options.hardware_mapping = 'regular'
matrix = RGBMatrix(options = options)

#============================================
#            TEXT CONFIG
#============================================
offscreen_canvas = matrix.CreateFrameCanvas()
font_time = graphics.Font()
#font.LoadFont("../fonts/texgyre-27.bdf")
font_time.LoadFont("../fonts/matrix_time-40.bdf")
font612 = graphics.Font()
font612.LoadFont("../fonts/clR6x12.bdf")
font57 = graphics.Font()
font57.LoadFont("../fonts/6x9.bdf")
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
#    matrix.Clear()
    offscreen_canvas.Clear()

    pos_x=0
#    pos_y=font.height
    pos_y=48
    color_R=0
    color_G=255
    color_B=0

    print(pos_y)

#============================================
#            READ SERIAL PORT
#============================================

#============================================
#            READ TEXT FILE
#============================================
    if(path.exists('/home/cvonselen/rpi-rgb-led-matrix/toprint.txt')):
        with open('/home/cvonselen/rpi-rgb-led-matrix/toprint.txt', 'r') as file:
            content = file.readlines()
            txt_to_print=content[0].decode('utf8')
            file.close()
    else :
        txt_to_print="0055"

    while True:

#============================================
#            READ SERIAL PORT
#============================================

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
                rx_time_min = rx_time[:2]
                rx_time_sec = rx_time[2:]

    #            print("rx_time:", rx_time)
    #            print("rx_timetype:", rx_timetype)
    #            print("rx_group:", rx_group)
    #            print("rx_round:", rx_round)
    #            print("rx_flight:", rx_flight)
    #            print("rx_task:", rx_task)
                ser.reset_input_buffer()
            except:
                print("Serial Error")

#============================================
#            DISPLAY TEXT
#============================================

            offscreen_canvas.Clear()
            if rx_timetype == 'Spare':
                graphics.DrawText(offscreen_canvas, font_time,0, pos_y,graphics.Color(255,0,255),rx_time_min)
                graphics.DrawText(offscreen_canvas, font_time,45,43,graphics.Color(255,0,255),":")
                graphics.DrawText(offscreen_canvas, font_time,50,48,graphics.Color(255,0,255),rx_time_sec)
                graphics.DrawText(offscreen_canvas, font612,0, 8,graphics.Color(255,0,255),"SPARE")
                graphics.DrawText(offscreen_canvas, font612,30, 8,graphics.Color(255,255,255),"R:" + rx_round +" Gr:" + rx_group)
                graphics.DrawText(offscreen_canvas, font57,0, 15,graphics.Color(255,255,255),rx_task)
#            offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
            if rx_timetype == 'Prep ':
                graphics.DrawText(offscreen_canvas, font_time,0, pos_y,graphics.Color(0,255,255),rx_time_min)
                graphics.DrawText(offscreen_canvas, font_time,45,43,graphics.Color(0,255,255),":")
                graphics.DrawText(offscreen_canvas, font_time,50,48,graphics.Color(0,255,255),rx_time_sec)
                graphics.DrawText(offscreen_canvas, font612,0, 8,graphics.Color(0,255,255),"PREP")
                graphics.DrawText(offscreen_canvas, font612,30, 8,graphics.Color(255,255,255),"R:" + rx_round +" Gr:" + rx_group)
                graphics.DrawText(offscreen_canvas, font57,0, 15,graphics.Color(255,255,255),rx_task)
#            offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
            if rx_timetype == 'NoFly':
                graphics.DrawText(offscreen_canvas, font_time,0, pos_y,graphics.Color(255,0,0),rx_time_min)
                graphics.DrawText(offscreen_canvas, font_time,45,43,graphics.Color(255,0,0),":")
                graphics.DrawText(offscreen_canvas, font_time,50,48,graphics.Color(255,0,0),rx_time_sec)
                graphics.DrawText(offscreen_canvas, font612,0, 8,graphics.Color(255,0,0),"NOFLY")
                graphics.DrawText(offscreen_canvas, font612,30, 8,graphics.Color(255,255,255),"R:" + rx_round +" Gr:" + rx_group)
                graphics.DrawText(offscreen_canvas, font57,0, 15,graphics.Color(255,255,255),rx_task)
#            offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
            if rx_timetype == 'Work ':
                graphics.DrawText(offscreen_canvas, font_time,0, pos_y,graphics.Color(0,255,0),rx_time_min)
                graphics.DrawText(offscreen_canvas, font_time,45,43,graphics.Color(0,255,0),":")
                graphics.DrawText(offscreen_canvas, font_time,50,48,graphics.Color(0,255,0),rx_time_sec)
                graphics.DrawText(offscreen_canvas, font612,0, 8,graphics.Color(0,255,0),"WORK")
                graphics.DrawText(offscreen_canvas, font612,30, 8,graphics.Color(255,255,255),"R:" + rx_round +" Gr:" + rx_group)
                graphics.DrawText(offscreen_canvas, font57,0, 15,graphics.Color(255,255,255),rx_task)
#            offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
            if rx_timetype == 'Land ':
                graphics.DrawText(offscreen_canvas, font_time,0, pos_y,graphics.Color(255,255,0),rx_time_min)
                graphics.DrawText(offscreen_canvas, font_time,45,43,graphics.Color(255,255,0),":")
                graphics.DrawText(offscreen_canvas, font_time,50,48,graphics.Color(255,255,0),rx_time_sec)
                graphics.DrawText(offscreen_canvas, font612,0, 8,graphics.Color(255,255,0),"LAND")
                graphics.DrawText(offscreen_canvas, font612,30, 8,graphics.Color(255,255,255),"R:" + rx_round +" Gr:" + rx_group)
                graphics.DrawText(offscreen_canvas, font57,0, 15,graphics.Color(255,255,255),rx_task)
            offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
            #time.sleep (1)
