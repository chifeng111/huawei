#coding:utf-8
#字符串运用-密码截取(算法复杂度太大)
import sys

def is_sym(s):
    n = len(s)
    if n%2 == 0:
        i = n//2 - 1
        j = i+1
        while i >= 0:
            if s[i] != s[j]:
                break
            i -= 1
            j += 1
        if i < 0:
            return True
    else:
        i = n//2 - 1
        j = i+2
        while i >= 0:
            if s[i] != s[j]:
                break
            i -= 1
            j += 1
        if i < 0:
            return True
    return False

try:
    while True:
        s = sys.stdin.readline().strip()
        if s == '':
            break
        n = int(len(s))
        max = 1
        for i in range(n-1):
            for j in range(n-1-i):
                new_s = s[i:i+j+2]
                if is_sym(new_s):
                    if len(new_s) > max:
                        max = len(new_s)
        print(max)

except:
    pass