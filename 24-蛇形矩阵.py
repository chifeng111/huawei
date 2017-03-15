#coding:utf-8
#打印蛇形矩阵
import sys

def snake(n):
    a = list(range(n))
    for i in range(n):
        a[i] = list(range(n-i))
    num = 1
    for i in range(n):
        m = i
        n = 0
        while m >= 0:
            a[m][n] = num
            num += 1
            m -= 1
            n += 1
    return a

try:
    while True:
        s = sys.stdin.readline().strip()
        if s == '':
            break
        n = int(s)
        a = snake(n)
        for i in a:
            b = [str(j) for j in i]
            print(' '.join(b))

except:
    pass