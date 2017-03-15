#coding:utf-8
#提取不重复的整数
import sys

try:
    while True:
        s = sys.stdin.readline().strip()
        if s == '':
            break
        n = len(s)
        s_new = ''
        for i in range(n):
            if s[-(i+1)] not in s_new:
                s_new += s[-(i+1)]
        print(s_new)



except:
    pass