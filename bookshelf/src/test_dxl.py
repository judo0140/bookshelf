#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dxl
#import dxl2

import os

if os.name == 'nt':
    import msvcrt
    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

dxl.bringup(1)
dxl.setting(1, 50, 20)
init_position=dxl.read(1).call()
dxl.bringup(2)
dxl.setting(2, 50, 20)
init_position2=dxl.read(2).call()
print(init_position)
#print(init_position)
#dxl.goal(1,0)
#dxl.bringup(2)
#dxl.setting(2, 50, 20)
#dxl2.bringup(1)
#dxl2.setting(1, 50, 20)
#read2=dxl.read(2)

while 1:
    print("Press key! (w/s/x/esc)")
    direction = getch()
    if direction == chr(0x1b):
        break

    elif direction == chr(0x77):
        dxl.goal(1, init_position+512)
        dxl.goal(2, init_position2+512)
#        dxl.goal(2, -500000)
#        dxl.goal(1, read1.call()-6500)
#        dxl2.goal(1, -50000)
#        dxl.goal(1, read1.call()+13795)
#        dxl.goal(2, read2.call()-13795)

    elif direction == chr(0x78):
        dxl.goal(1, init_position-512)
        dxl.goal(2, init_position2-512)
#        dxl.goal(2, 500000)
#        dxl.goal(1, read1.call()+6500)
#        dxl2.goal(1,50000)

    elif direction == chr(0x73):
        dxl.goal(1, init_position)
        dxl.goal(2, init_position2)
#        dxl.stop(1)
#        dxl.stop(2)
#        dxl2.stop(1)
#        dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, 3, ADDR_PRESENT_POSITION)
#        dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL_ID, ADDR_GOAL_POSITION, dxl_present_position)
#        print("PresPos-3 : %01d" % (dxl_present_position) )



