#coding:utf-8
#质数因子
import sys

try:
    while True:
        s1 = sys.stdin.readline().strip()
        if s1 == '':
            break
        num = int(s1)
        l = []
        i = 2
        while i <= num:
            if num%i == 0:
                l.append(i)
                num /= i
                continue
            i += 1
        s = ''
        for i in l:
            s += str(i)
            s += ' '
        print(s)


except:
    pass