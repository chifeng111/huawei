#coding:utf-8
#字符串分割
import sys
import re

def divi(s):
    a = re.findall('.{8}', s)
    n = (len(s))%8
    if n != 0:
        b = s[-n:]
        for i in range(8-n):
            b += '0'
        a.append(b)
    return a


try:
    while True:
        s1 = sys.stdin.readline().strip()
        if s1 == '':
            break
        s2 = sys.stdin.readline().strip()
        l1 = divi(s1)
        l2 = divi(s2)
        for i in l1:
            print(i)
        for j in l2:
            print(j)

except:
    pass