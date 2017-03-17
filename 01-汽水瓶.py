#coding:utf-8
#汽水瓶

def fun(em_b):
    exch_t = 0
    while em_b > 2:
        exch = em_b//3
        exch_t += exch
        em_b = em_b%3 + exch

    if em_b == 2:
        exch_t += 1

    return exch_t


try:
    while 1:
        em_b = int(input())
        if em_b != 0:
            print(fun(em_b))
        else:
            break
except:
    pass

