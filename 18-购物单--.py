#coding:utf-8
#购物单

import sys

try:
    while True:
        s = sys.stdin.readline().strip()
        if s == '':
            break
        N = int(s.split(" ")[0])
        m = int(s.split(" ")[1])
        l = [["", "", ""]]
        for i in range(m):
            ss = sys.stdin.readline().strip()
            v = int(ss.split(" ")[0])
            p = int(ss.split(" ")[1])
            q = int(ss.split(" ")[2])
            l.append([v, p, q])
        #剩余的钱money，买前n样东西的最大价值n = 1,2,3,4,5...
        def getmaxvalue(money, n):
            if n == 1:
                if money >= l[1][0]:
                    return l[1][0]*l[1][1]
                else:
                    return 0
            elif money >= l[n][0]:
                return max(getmaxvalue(money-l[n][0], n-1) + l[n][0]*l[n][1], getmaxvalue(money, n-1))
            else:
                return getmaxvalue(money, n-1)
        print(getmaxvalue(N, m))

except:
    pass