#coding:utf-8
#自守数
import sys

def check(num):
    s = str(num**2)
    num =str(num)
    n = len(num)
    if s[-n:] ==num:
        return True
    else:
        return False


try:
    while True:
        s1 = sys.stdin.readline().strip()
        if s1 == '':
            break
        n = int(s1)
        count = 0
        for i in range(n):
            if check(i+1):
                count += 1
        print(count)


except:
    pass