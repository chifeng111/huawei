#-*- coding:utf-8 -*-
#数字颠倒

import sys

try:
    while 1:
        s = sys.stdin.readline().strip()
        if s == "":
            break
        n = len(s)
        new_s = ''
        for i in range(n):
            new_s += s[-i-1]
        print(new_s)


except:
    pass