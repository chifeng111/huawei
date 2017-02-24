#-*- coding:utf-8 -*-
#句子逆序

import sys

try:
    while 1:
        s = sys.stdin.readline().strip()
        if s == "":
            break
        l = s.split(' ')
        new_l = reversed(l)
        ss = ''
        for i in new_l:
            ss += i
            ss += ' '
        ss = ss[:-1]
        print(ss)


except:
    pass