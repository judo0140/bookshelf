#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dxl
import os

# class 설명
# dxl.bringup(dxl_id) : 다이나믹셀 구동 위한 bringup class .. ex) dxl.bringup(1) = ID:1 인 다이나믹셀 구동 준비
# dxl.setting(dxl_id, velocity, acceleration) : 다이나믹셀 구동 회전 속도, 가속도 설정 .. ex) dxl.bringup(1, 50, 20) = ID:1 인 다이나믹셀 속도 50, 가속도 20으로 설정
# dxl.goal(dxl_id, goal_psition) : 다이나믹셀에 목표 위치 명령 .. ex) dxl.goal(1, 3000) = ID:1 인 다이나믹셀을 위치값 3000인 위치로 회전
# dxl.stop(dxl_id) : 다이나믹셀 구동 중지 .. ex) dxl.stop(1) = ID:1 인 다이나믹셀 구동 중지
# dxl.read(dxl_id).call() : 다이나믹셀 현재 위치값 읽어오기 .. ex) dxl.read(1).call() = ID:1 인 다이나믹셀 현재 위치값 읽어오기

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

