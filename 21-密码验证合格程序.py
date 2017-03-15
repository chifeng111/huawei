#coding:utf-8
#密码验证合格程序
import sys

def check(pwd):
    n = len(pwd)
    if n < 8:
        return False
    flag = [0, 0, 0, 0]
    for i in pwd:
        if 'a' <= i <= 'z':
            flag[0] = 1
        elif 'A' <= i <= 'Z':
            flag[1] = 1
        elif '0' <= i <= '9':
            flag[2] = 1
        else:
            flag[3] = 1
    #print(sum(flag))
    if sum(flag) < 3:
        return False
    for i in range(n-5):
        for j in range(n-i-5):
            if pwd[i] == pwd[i+j+3] and pwd[i+1] == pwd[i+j+4] and pwd[i+2] == pwd[i+j+5]:
                return False
    return True

try:
    out = []
    while True:
        s = sys.stdin.readline().strip()
        if s == '':
            break
        if check(s):
            out.append('OK')
        else:
            out.append('NG')
    for i in out:
        print(i)

except:
    pass