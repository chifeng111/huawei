# -*- coding:utf-8 -*-
#循环单词
import sys

def check(w1, w2):
    if len(w1) != len(w2):
        return False
    n = len(w1)
    for i in range(n-1):
        w2 = w2[1:] + w2[0]
        if w2 == w1:
            return True
    return False

try:
    while True:
        s = sys.stdin.readline().strip()
        if s == '':
            break
        n = int(s)
        word = []
        for i in range(n):
            word.append(sys.stdin.readline().strip())
        cycle_type = 1
        #cycled_word = []
        for i in range(n-1):
            j = i+1
            while j < n:
                if check(word[i], word[j]):
                    break
                j += 1
            if j >= n:
                cycle_type += 1
        print(cycle_type)
except:
    pass