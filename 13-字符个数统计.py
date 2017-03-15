#-*- coding:utf-8 -*-
#字符个数统计

import sys

try:
    while 1:
        s = sys.stdin.readline().strip()
        if s == "":
            break
        n = len(s)
        new_s = []
        for i in range(n):
            if 0<=ord(s[i])<=127:
                if s[i] not in new_s:
                    new_s.append(s[i])
        print(len(new_s))


except:
    pass