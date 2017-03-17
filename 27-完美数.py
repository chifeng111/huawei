# -*- coding:utf-8 -*-
#完美数
import sys

def is_perfect_number(n):
    l = []
    for i in range(1, n//2+1):
        if n%i == 0:
            l.append(i)
    if sum(l) == n:
        return True
    return False


try:
    while True:
        s = sys.stdin.readline().strip()
        if s == '':
            break
        n = int(s)
        count = 0
        for i in range(1, n+1):
            if is_perfect_number(i):
                #print(i)
                count += 1
        print(count)
except:
    pass