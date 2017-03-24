# -*- coding:utf-8 -*-
#超级素数幂
import sys
import math
#查找n以内的素数并返回列表
def find_zishu(n):
    l = [2]
    for i in range(3, n+1):
        is_prime = True
        s = int(math.sqrt(i))
        for j in range(2, s+1):
            if i%j == 0:
                is_prime = False
                break
        if is_prime:
            l.append(i)
    return l

def find_pq(n):
    flag = False
    P = Q = 0
    l = find_zishu(n//2)
    for i in l:
        q = 2
        while i**q <= n:
            if i**q == n:
                break
            q += 1
        if i**q == n:
            flag = True
            P = i
            Q = q
            break
    return [flag, P, Q]

try:
    while True:
        s = sys.stdin.readline().strip()
        if s == '':
            break
        n = int(s)
        #print(find_zishu(n))
        l = find_pq(n)
        if l[0]:
            print('%s %s' %(l[1], l[2]))
        else:
            print('No')


except:
    pass