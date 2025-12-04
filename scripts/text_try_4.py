#!/usr/bin/python
# SIMPLE TEXT DISPLAY FROM TEXT FILE
# Autor : A.HALET


import time
import sys
import os

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from os import path


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
#options.limit_refresh_rate_hz = 700
options.row_address_type = 2
options.pwm_lsb_nanoseconds = 130
#options.pixel_mapper_config = "V-mapper;Rotate:-90"
#options.disable_hardware_pulsing = 1
options.pwm_bits = 1
options.hardware_mapping = 'regular'
matrix = RGBMatrix(options = options)

#============================================
#            TEXT CONFIG
#============================================
offscreen_canvas = matrix.CreateFrameCanvas()
font = graphics.Font()
#font.LoadFont("../fonts/texgyre-27.bdf")
font.LoadFont("../fonts/matrix_time-40.bdf")
font57 = graphics.Font()
font57.LoadFont("../fonts/clR6x12.bdf")
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
#            DISPLAY TEXT
#============================================
 #       len_pic = graphics.DrawText(offscreen_canvas, font,pos_x, pos_y,graphics.Color(color_R,color_G,color_B),txt_to_print)
 #       graphics.DrawText(offscreen_canvas, font,0, pos_y,graphics.Color(255,0,0),txt_to_print)
 #       graphics.DrawText(offscreen_canvas, font57,pos_x, 8,graphics.Color(color_R,color_G,color_B),"Hello world 12345")
#        pos -= 1
#        if (pos + len_pic < 0):
#            pos = offscreen_canvas.width
#        time.sleep(0.01)
#        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
#        time.sleep (1)
        offscreen_canvas.Clear()
        graphics.DrawText(offscreen_canvas, font,0, pos_y,graphics.Color(255,0,0),"00")
        graphics.DrawText(offscreen_canvas, font,45,43,graphics.Color(255,0,0),":")
        graphics.DrawText(offscreen_canvas, font,50,48,graphics.Color(255,0,0),"59")
        graphics.DrawText(offscreen_canvas, font57,pos_x, 17,graphics.Color(color_R,color_G,color_B),graphics.Color(0,255,0),"WORK")
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
        time.sleep (1)
        offscreen_canvas.Clear()
        graphics.DrawText(offscreen_canvas, font,0, pos_y,graphics.Color(255,0,0),"00")
        graphics.DrawText(offscreen_canvas, font,45,43,graphics.Color(255,0,0),":")
        graphics.DrawText(offscreen_canvas, font,50,48,graphics.Color(255,0,0),"58")
        graphics.DrawText(offscreen_canvas, font57,pos_x, 17,graphics.Color(color_R,color_G,color_B),"WORK")
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
        time.sleep (1)
        offscreen_canvas.Clear()
        graphics.DrawText(offscreen_canvas, font,0, pos_y,graphics.Color(255,0,0),"00")
        graphics.DrawText(offscreen_canvas, font,45,43,graphics.Color(255,0,0),":")
        graphics.DrawText(offscreen_canvas, font,50,48,graphics.Color(255,0,0),"47")
        graphics.DrawText(offscreen_canvas, font57,pos_x, 17,graphics.Color(color_R,color_G,color_B),"WORK")
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
        time.sleep (1)
        offscreen_canvas.Clear()
        graphics.DrawText(offscreen_canvas, font,0, pos_y,graphics.Color(255,0,0),"00")
        graphics.DrawText(offscreen_canvas, font,45,43,graphics.Color(255,0,0),":")
        graphics.DrawText(offscreen_canvas, font,50,48,graphics.Color(255,0,0),"46")
        graphics.DrawText(offscreen_canvas, font57,pos_x, 17,graphics.Color(color_R,color_G,color_B),"WORK")
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
        time.sleep (1)
        offscreen_canvas.Clear()
        graphics.DrawText(offscreen_canvas, font,0, pos_y,graphics.Color(255,0,0),"10")
        graphics.DrawText(offscreen_canvas, font,45,43,graphics.Color(255,0,0),":")
        graphics.DrawText(offscreen_canvas, font,50,48,graphics.Color(255,0,0),"35")
        graphics.DrawText(offscreen_canvas, font57,pos_x, 17,graphics.Color(color_R,color_G,color_B),"WORK")
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
        time.sleep (1)
        offscreen_canvas.Clear()
        graphics.DrawText(offscreen_canvas, font,0, pos_y,graphics.Color(255,0,0),"10")
        graphics.DrawText(offscreen_canvas, font,45,43,graphics.Color(255,0,0),":")
        graphics.DrawText(offscreen_canvas, font,50,48,graphics.Color(255,0,0),"34")
        graphics.DrawText(offscreen_canvas, font57,pos_x, 17,graphics.Color(color_R,color_G,color_B),"WORK")
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
        time.sleep (1)
        offscreen_canvas.Clear()
        graphics.DrawText(offscreen_canvas, font,0, pos_y,graphics.Color(255,0,0),"10")
        graphics.DrawText(offscreen_canvas, font,45,43,graphics.Color(255,0,0),":")
        graphics.DrawText(offscreen_canvas, font,50,48,graphics.Color(255,0,0),"23")
        graphics.DrawText(offscreen_canvas, font57,pos_x, 17,graphics.Color(color_R,color_G,color_B),"WORK")
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
        time.sleep (1)
        offscreen_canvas.Clear()
        graphics.DrawText(offscreen_canvas, font,0, pos_y,graphics.Color(255,0,0),"10")
        graphics.DrawText(offscreen_canvas, font,45,43,graphics.Color(255,0,0),":")
        graphics.DrawText(offscreen_canvas, font,50,48,graphics.Color(255,0,0),"12")
        graphics.DrawText(offscreen_canvas, font57,pos_x, 17,graphics.Color(color_R,color_G,color_B),"WORK")
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
        time.sleep (1)
        offscreen_canvas.Clear()
        graphics.DrawText(offscreen_canvas, font,0, pos_y,graphics.Color(255,0,0),"10")
        graphics.DrawText(offscreen_canvas, font,45,43,graphics.Color(255,0,0),":")
        graphics.DrawText(offscreen_canvas, font,50,48,graphics.Color(255,0,0),"11")
        graphics.DrawText(offscreen_canvas, font57,pos_x, 17,graphics.Color(color_R,color_G,color_B),"WORK")
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
        time.sleep (1)
        offscreen_canvas.Clear()
        graphics.DrawText(offscreen_canvas, font,0, pos_y,graphics.Color(255,0,0),"10")
        graphics.DrawText(offscreen_canvas, font,45,43,graphics.Color(255,0,0),":")
        graphics.DrawText(offscreen_canvas, font,50,48,graphics.Color(255,0,0),"01")
        graphics.DrawText(offscreen_canvas, font57,pos_x, 17,graphics.Color(color_R,color_G,color_B),"WORK")
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
        time.sleep (1)
        offscreen_canvas.Clear()
        graphics.DrawText(offscreen_canvas, font,0, pos_y,graphics.Color(255,0,0),"00")
        graphics.DrawText(offscreen_canvas, font,45,43,graphics.Color(255,0,0),":")
        graphics.DrawText(offscreen_canvas, font,50,48,graphics.Color(255,0,0),"00")
        graphics.DrawText(offscreen_canvas, font57,pos_x, 17,graphics.Color(color_R,color_G,color_B),"WORK")
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
        time.sleep (1)
        offscreen_canvas.Clear()
