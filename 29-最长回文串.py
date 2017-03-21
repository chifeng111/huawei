# -*- coding:utf-8 -*-
#最长回文串
import sys
def get_huiwen(s):
    n = len(s)
    if n == 1:
        return 1
    #aba类型
    l1 = []
    i = 0
    while i < n:
        j = 0
        while i-j >= 0 and i+j < n:
            if s[i-j] != s[i+j]:
                l1.append(j)
                break
            if i-j == 0 or i+j == n-1:
                l1.append(j+1)
            j += 1
        i += 1
    aba = max(l1)*2 - 1
    #abba类型
    l2 = []
    i = 0
    while i < n:
        j = 0
        while i-j >= 0 and i+j+1 < n:
            if s[i-j] != s[i+j+1]:
                l2.append(j)
                break
            if i-j == 0 or i+j+1 == n-1:
                l2.append(j+1)
            j += 1
        i += 1
    abba = max(l2)*2
    return max([aba, abba])


try:
    while True:
        s = sys.stdin.readline().strip()
        if s == '':
            break
        print(get_huiwen(s))
except:
    pass