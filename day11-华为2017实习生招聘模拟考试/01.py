import sys

try:
    while True:
        s = sys.stdin.readline().strip()
        if s == '':
            break
        a = int(s.split(" ")[0])
        b = int(s.split(" ")[1])
        print(a+b)
except:
    pass