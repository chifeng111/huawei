# -*- coding:utf-8 -*-
#连续整数
import sys
def out(num, n):
    if max(num)-min(num) == n:
        if len(set(num)) == len(num):
            for i in range(min(num), max(num)+1):
                if i not in num:
                    print(i)
        else:
            print('mistake')
    elif max(num)-min(num) == n-1:
        if len(set(num)) == len(num):
            if min(num) == 1:
                print('%d' %(max(num)+1))
            else:
                print('%d %d' %(min(num)-1, max(num)+1))
        else:
            print('mistake')
    else:
        print('mistake')

try:
    while True:
        s = sys.stdin.readline().strip()
        if s == '':
            break
        n = int(s)
        s1 = sys.stdin.readline().strip()
        num = s1.split(" ")
        num = [int(i) for i in num]
        out(num, n)
except:
    pass