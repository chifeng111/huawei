#coding:utf-8
#简单密码
import sys

def new_pwd(s):
    n_s = ''
    for i in s:
        if 'a' <= i <= 'c':
            n_s += '2'
        elif 'd' <= i <= 'f':
            n_s += '3'
        elif 'g' <= i <= 'i':
            n_s += '4'
        elif 'j' <= i <= 'l':
            n_s += '5'
        elif 'm' <= i <= 'o':
            n_s += '6'
        elif 'p' <= i <= 's':
            n_s += '7'
        elif 't' <= i <= 'v':
            n_s += '8'
        elif 'w' <= i <= 'z':
            n_s += '9'
        elif 'A' <= i <= 'Z':
            if i == 'Z':
                n_s += 'a'
            else:
                n_s += chr(ord(i)+1).lower()
        else:
            n_s += i
    return n_s


try:
    while True:
        s = sys.stdin.readline().strip()
        if s == '':
            break
        print(new_pwd(s))
except:
    pass