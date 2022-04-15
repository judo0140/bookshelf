#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dxl
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

while 1:
    print("Press key! (w/s/x/esc)")
    direction = getch()
    if direction == chr(0x1b):
        break

    # 'w' 입력 시
    elif direction == chr(0x77):
        dxl.goal(1, init_position+512)
        dxl.goal(2, init_position2+512)

    # 'x' 입력 시
    elif direction == chr(0x78):
        dxl.goal(1, init_position-512)
        dxl.goal(2, init_position2-512)

    # 's' 입력 시
    elif direction == chr(0x73):
        dxl.goal(1, init_position)
        dxl.goal(2, init_position2)

