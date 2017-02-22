#coding:utf-8
#取近似值
import sys

try:
    while True:
        s1 = sys.stdin.readline().strip()
        if s1 == '':
            break
        s1 = str(float(s1))
        n = int(s1.split(".")[0])
        m = s1.split(".")[1]
        if int(m[0]) > 4:
            print(n+1)
        else:
            print(n)


except:
    pass