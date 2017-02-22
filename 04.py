#coding:utf-8
#明明的随机数
import sys

try:
    while True:
        n = sys.stdin.readline().strip()
        if n == '':
            break
        n = int(n)
        inputArray = []
        for i in range(n):
            inputDate = int(sys.stdin.readline().strip())
            inputArray.append(inputDate)
        #print(inputArray)
        inputArray.sort()
        OutputArray = []
        for i in inputArray:
            if i not in OutputArray:
                OutputArray.append(i)
        #print(OutputArray)
        for i in OutputArray:
            print(i)
except:
    pass