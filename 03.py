#-*- coding:utf-8 -*-
#扑克牌大小

import sys
def get_value(s):
    if s == 'J':
        return 11
    elif s == 'Q':
        return 12
    elif s == 'K':
        return 13
    elif s == "A":
        return 14
    elif s == "2":
        return 15
    else:
        return int(s)


try:
    while 1:
        input_ = sys.stdin.readline().strip()
        if input_ == "":
            break
        A = input_.split("-")[0]
        B = input_.split("-")[1]
        if A == 'joker JOKER' or B == 'joker JOKER':
            if A == 'joker JOKER':
                print(A)
            else:
                print(B)
        elif len(A.split(" ")) == len(B.split(" ")):
            if get_value(A.split(" ")[0]) > get_value(B.split(" ")[0]):
                print(A)
            else:
                print(B)
        elif len(A.split(" ")) == 4 or len(B.split(" ")) == 4:
            if len(A.split(" ")) == 4:
                print(A)
            else:
                print(B)
        else:
            print("ERROR")

except:
    pass