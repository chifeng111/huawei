# -*- coding:utf-8 -*-
#挑7
import sys

try:
    while True:
        s = sys.stdin.readline().strip()
        if s == '':
            break
        n = int(s)
        num = 0
        for i in range(1, n+1):
            if '7' in str(i) or i%7 == 0:
                num += 1
        print(num)
except:
    pass