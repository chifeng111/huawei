# -*- coding:utf-8 -*-
#好多鱼
import sys
def can_put(size, fishSize):
    for i in fishSize:
        if 2*size <= i <= 10*size or 2*i <= size <= 10*i:
            return False
    return True

try:
    while True:
        s = sys.stdin.readline().strip()
        if s == '':
            break
        minSize = int(s.split(" ")[0])
        maxSize = int(s.split(" ")[1])
        n = int(sys.stdin.readline().strip())
        s3 = sys.stdin.readline().strip()
        fishSize = s3.split(" ")
        fishSize = [int(i) for i in fishSize]
        num = 0
        for i in range(minSize, maxSize+1):
            if can_put(i, fishSize):
                num += 1
        print(num)

except:
    pass