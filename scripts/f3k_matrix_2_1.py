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


pilots = {}
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
#options.show_refresh_rate = 1
options.limit_refresh_rate_hz = 1700
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



    while True:

#============================================
#            READ SERIAL PORT
#============================================

        if ser.in_waiting >0:
            line = ()
            try: 
                line = ser.readline().decode ('utf-8').rstrip()
 #               ser.reset_input_buffer()
                print(line)
            except:
                print("Error in serial read")
            try:
                jsonObj = json.loads(line)
                rx_t = jsonObj.get('t')
                print(rx_t)
            except:
                print("Serial Error")
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                # IF THE t value is time we precess the time packet and display it
                #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #    try:
            if rx_t == 'time':
                rx_d = jsonObj.get('d')
                rx_slot_time = jsonObj['d']['slot_time']
                rx_no_fly = jsonObj['d']['no_fly']
                rx_time_s = jsonObj['d']['time_s']
                rx_r_num = jsonObj['d']['r_num']
                rx_r_num = str(rx_r_num)
                rx_g_let = jsonObj['d']['g_let']
                rx_f_num = jsonObj['d']['f_num']
                rx_sect = jsonObj['d']['sect']
                rx_task_name = jsonObj['d']['task_name']
                rx_task_name = rx_task_name[13:]
                rx_time_min = rx_time_s[:2]
                rx_time_sec = rx_time_s[3:]
                print("rx_time_s:", rx_time_s)
                print("rx_sect:", rx_sect)
                print("rx_g_let:", rx_g_let)
                print("rx_r_num:", rx_r_num)
                print("rx_f_num:", rx_f_num)
                print("rx_task_name:", rx_task_name)
                #============================================
                # DISPLAY TIME 
                #============================================

                offscreen_canvas.Clear()
                if rx_sect == 'Actual Time HH:MM':
                    graphics.DrawText(offscreen_canvas, font_time,0, pos_y,graphics.Color(255,0,255),rx_time_min)
                    graphics.DrawText(offscreen_canvas, font_time,45,43,graphics.Color(255,0,255),":")
                    graphics.DrawText(offscreen_canvas, font_time,50,48,graphics.Color(255,0,255),rx_time_sec)
                    graphics.DrawText(offscreen_canvas, font612,0, 8,graphics.Color(255,0,255),"TIME OF DAY")
                 #   graphics.DrawText(offscreen_canvas, font612,30, 8,graphics.Color(255,255,255),"R:" + rx_r_num +" Gr:" + rx_g_let)
                 #   graphics.DrawText(offscreen_canvas, font57,0, 15,graphics.Color(255,255,255),'Time of Day')
                if rx_sect == 'Waiting for next group':
                    graphics.DrawText(offscreen_canvas, font_time,0, pos_y,graphics.Color(255,0,255),rx_time_min)
                    graphics.DrawText(offscreen_canvas, font_time,45,43,graphics.Color(255,0,255),":")
                    graphics.DrawText(offscreen_canvas, font_time,50,48,graphics.Color(255,0,255),rx_time_sec)
                    graphics.DrawText(offscreen_canvas, font612,0, 8,graphics.Color(255,0,255),"WAIT")
                    graphics.DrawText(offscreen_canvas, font612,30, 8,graphics.Color(255,255,255),"R:" + rx_r_num +" Gr:" + rx_g_let)
                    graphics.DrawText(offscreen_canvas, font57,0, 15,graphics.Color(255,255,255),rx_task_name)
                if rx_sect == 'Announcement in progress':
                    #graphics.DrawText(offscreen_canvas, font_time,0, pos_y,graphics.Color(255,0,255),rx_time_min)
                    #graphics.DrawText(offscreen_canvas, font_time,45,43,graphics.Color(255,0,255),":")
                    #graphics.DrawText(offscreen_canvas, font_time,50,48,graphics.Color(255,0,255),rx_time_sec)
                    graphics.DrawText(offscreen_canvas, font612,0, 8,graphics.Color(255,0,255),"SPEAK")
                    graphics.DrawText(offscreen_canvas, font612,30, 8,graphics.Color(255,255,255),"R:" + rx_r_num +" Gr:" + rx_g_let)
                    graphics.DrawText(offscreen_canvas, font57,0, 15,graphics.Color(255,255,255),rx_task_name)
    #            offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
                if rx_sect == 'Preparation Time':
                    graphics.DrawText(offscreen_canvas, font_time,0, pos_y,graphics.Color(0,255,255),rx_time_min)
                    graphics.DrawText(offscreen_canvas, font_time,45,43,graphics.Color(0,255,255),":")
                    graphics.DrawText(offscreen_canvas, font_time,50,48,graphics.Color(0,255,255),rx_time_sec)
                    graphics.DrawText(offscreen_canvas, font612,0, 8,graphics.Color(0,255,255),"PREP")
                    graphics.DrawText(offscreen_canvas, font612,30, 8,graphics.Color(255,255,255),"R:" + rx_r_num +" Gr:" + rx_g_let)
                    graphics.DrawText(offscreen_canvas, font57,0, 15,graphics.Color(255,255,255),rx_task_name)
    #            offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
                if rx_sect == 'No Fly Time':
                    graphics.DrawText(offscreen_canvas, font_time,0, pos_y,graphics.Color(255,0,0),rx_time_min)
                    graphics.DrawText(offscreen_canvas, font_time,45,43,graphics.Color(255,0,0),":")
                    graphics.DrawText(offscreen_canvas, font_time,50,48,graphics.Color(255,0,0),rx_time_sec)
                    graphics.DrawText(offscreen_canvas, font612,0, 8,graphics.Color(255,0,0),"NOFLY")
                    graphics.DrawText(offscreen_canvas, font612,30, 8,graphics.Color(255,255,255),"R:" + rx_r_num +" Gr:" + rx_g_let)
                    graphics.DrawText(offscreen_canvas, font57,0, 15,graphics.Color(255,255,255),rx_task_name)
    #            offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
                if rx_sect == 'Working Time':
                    graphics.DrawText(offscreen_canvas, font_time,0, pos_y,graphics.Color(0,255,0),rx_time_min)
                    graphics.DrawText(offscreen_canvas, font_time,45,43,graphics.Color(0,255,0),":")
                    graphics.DrawText(offscreen_canvas, font_time,50,48,graphics.Color(0,255,0),rx_time_sec)
                    graphics.DrawText(offscreen_canvas, font612,0, 8,graphics.Color(0,255,0),"WORK")
                    graphics.DrawText(offscreen_canvas, font612,30, 8,graphics.Color(255,255,255),"R:" + rx_r_num +" Gr:" + rx_g_let)
                    graphics.DrawText(offscreen_canvas, font57,0, 15,graphics.Color(255,255,255),rx_task_name)
    #            offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
                if rx_sect == 'Landing Window':
                    graphics.DrawText(offscreen_canvas, font_time,0, pos_y,graphics.Color(255,255,0),rx_time_min)
                    graphics.DrawText(offscreen_canvas, font_time,45,43,graphics.Color(255,255,0),":")
                    graphics.DrawText(offscreen_canvas, font_time,50,48,graphics.Color(255,255,0),rx_time_sec)
                    graphics.DrawText(offscreen_canvas, font612,0, 8,graphics.Color(255,255,0),"LAND")
                    graphics.DrawText(offscreen_canvas, font612,30, 8,graphics.Color(255,255,255),"R:" + rx_r_num +" Gr:" + rx_g_let)
                    graphics.DrawText(offscreen_canvas, font57,0, 15,graphics.Color(255,255,255),rx_task_name)
                offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # IF THE t value is pilot definition we process the id and pilot name and store it in a dictionary called pilots
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #    try:
            if rx_t == 'p_def':
                rx_pilot_id = jsonObj['d']['id']
                rx_pilot_name = jsonObj['d']['name']
                pilots[rx_pilot_id] = rx_pilot_name
            

            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # IF THE t value is pilot definition we process the id and pilot name and store it in a dictionary called pilots
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #    try:
            if rx_t == 'p_list':
                rx_group_pilot_list = jsonObj['d']
                pilot_line_pos_y = 15
                offscreen_canvas.Clear()
                for pilot_id in rx_group_pilot_list:
                    pilot_name =  pilots[pilot_id]
                    graphics.DrawText(offscreen_canvas, font612,0, 8,graphics.Color(255,255,0),"Pilots")
                    graphics.DrawText(offscreen_canvas, font612,40, 8,graphics.Color(255,255,255),"R:" + rx_r_num +" Gr:" + rx_g_let)
                   # graphics.DrawText(offscreen_canvas, font57,0, 15,graphics.Color(255,255,255),rx_task_name)
                    graphics.DrawText(offscreen_canvas, font57,0, pilot_line_pos_y,graphics.Color(255,255,255),pilot_name)
                    pilot_line_pos_y = pilot_line_pos_y + 7
                offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
                time.sleep(15)
                ser.reset_input_buffer()