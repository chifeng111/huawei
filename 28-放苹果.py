# -*- coding:utf-8 -*-
#放苹果
import sys

def put_apples(m, n):
    if m <0:
        return 0
    if m==1 or n==1:
        return 1
    return put_apples(m, n-1)+put_apples(m-n, n)

try:
    while True:
        s = sys.stdin.readline().strip()
        if s == '':
            break
        m = int(s.split(" ")[0])
        n = int(s.split(" ")[1])
        print(put_apples(m, n))
except:
    pass