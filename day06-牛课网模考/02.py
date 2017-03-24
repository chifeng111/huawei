__author__ = 'zhenhua'
import sys

n = sys.stdin.readline().strip()
n = int(n)
l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(1,n+1):
    s = str(i)
    for j in s:
        l[int(j)] += 1

ll = []
for i in l:
    ll.append(str(i))
print(' '.join(ll))

