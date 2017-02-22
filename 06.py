#coding:utf-8
#进制转换
import sys
import re
def get_value(s):
    if s in ['A', 'B', 'C', 'D', 'E', 'F']:
        return ord(s)-55
    return int(s)

def ox(s):
    new_s = s[2:]
    n = len(new_s)
    value = 0
    for i in range(n):
        value += get_value(new_s[i])*(16**(n-i-1))
    return value

try:
    while True:
        s1 = sys.stdin.readline().strip()
        if s1 == '':
            break
        print(ox(s1))

except:
    pass