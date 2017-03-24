import sys

def poke(s, n):
    letf = [val for idx, val in enumerate(s) if idx < n]
    right = [val for idx, val in enumerate(s) if idx >= n]
    new_l = []
    for i in range(n):
        new_l.append(letf[i])
        new_l.append(right[i])
    return new_l

try:
    s1 = int(sys.stdin.readline().strip())
    for i in range(s1):
        s2 = sys.stdin.readline().strip()
        n = int(s2.split(" ")[0])
        k = int(s2.split(" ")[1])
        s3 = sys.stdin.readline().strip()
        l = s3.split(" ")
        for j in range(k):
            l = poke(l, n)
        print(' '.join(l))

except:
    pass