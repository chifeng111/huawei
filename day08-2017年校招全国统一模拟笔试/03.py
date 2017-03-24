# -*- coding:utf-8 -*-
#DNA合成
import sys

def check(s1, s2):
    if s1 == 'A' and s2 == 'T':
        return True
    elif s1 == 'T' and s2 == 'A':
        return True
    elif s1 == 'C' and s2 == 'G':
        return True
    elif s1 == 'G' and s2 == 'C':
        return True
    return False

try:
    while True:
        s = sys.stdin.readline().strip()
        if s == '':
            break
        s1 = s.split(" ")[0]
        s2 = s.split(" ")[1]
        n = len(s1)
        num =0
        for i in range(n):
            if not check(s1[i], s2[i]):
                num += 1
        print(num)
except:
    pass