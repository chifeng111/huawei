# -*- coding:utf-8 -*-
#四则运算
import sys

try:
    while True:
        s = sys.stdin.readline().strip()
        if s == '':
            break
        new_s = ''
        for i in s:
            if i == '[' or i == '{':
                new_s += '('
            elif i == ']' or i == '}':
                new_s += ')'
            else:
                new_s += i
        new_s = 'print(' + new_s + ')'
        exec(new_s)
except:
    pass