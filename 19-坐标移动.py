#-*- coding:utf-8 -*-
#坐标移动

import sys

def is_num(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

try:
    while 1:
        s = sys.stdin.readline().strip()
        if s == "":
            break
        order = s.split(";")
        x = 0
        y = 0
        for o in order:
            if o == '':
                pass
            elif o[0] == 'A' and is_num(o[1:]):
                x -= int(o[1:])
            elif o[0] == 'D' and is_num(o[1:]):
                x += int(o[1:])
            elif o[0] == 'W' and is_num(o[1:]):
                y += int(o[1:])
            elif o[0] == 'S' and is_num(o[1:]):
                y -= int(o[1:])
            else:
                pass
        print("%s,%s" %(x,y))
except:
    pass