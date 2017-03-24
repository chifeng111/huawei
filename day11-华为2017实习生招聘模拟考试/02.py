import sys
#超时
def fuc(a, b, c):
    count = 0
    for i in range(a, b+1):
        if i%c == 0:
            count += 1
    return count

try:
    while True:
        s = sys.stdin.readline().strip()
        if s == '':
            break
        a = int(s.split(" ")[0])
        b = int(s.split(" ")[1])
        c = int(s.split(" ")[2])
        print(fuc(a, b, c))
except:
    pass