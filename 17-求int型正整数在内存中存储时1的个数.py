#coding:utf-8
#求int型正整数在内存中存储时1的个数

import sys

try:
    while True:
        s = sys.stdin.readline().strip()
        if s == '':
            break
        out = bin(int(s))
        out =out[2:]
        count = 0
        for i in out:
            if i == '1':
                count += 1
        print(count)
except:
    pass