#coding:utf-8
#合并表记录
import sys

try:
    while True:
        s1 = sys.stdin.readline().strip()
        if s1 == '':
            break
        n = int(s1)
        d = {}
        for i in range(n):
            s = sys.stdin.readline().strip()
            a=int(s.split(" ")[0])
            b=int(s.split(" ")[1])
            if a in d.keys():
                d[a]+=b
            else:
                d[a]=b
        s = sorted(d.keys())
        for i in s:
            print("%s %s" %(i,d[i]))



except:
    pass