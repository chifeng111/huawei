#-*- coding:utf-8 -*-
#字符串连接最长路径查找

import sys

try:
    while 1:
        s = sys.stdin.readline().strip()
        if s == "":
            break
        n = int(s)
        l = []
        for i in range(n):
            l.append(sys.stdin.readline().strip())
        for i in range(n-1):
            for j in range(n-1-i):
                if l[j].upper() > l[j+1].upper():
                    l[j], l[j+1] = l[j+1], l[j]
        for i in range(n):
            print(l[i])


except:
    pass