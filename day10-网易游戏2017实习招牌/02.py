import sys

s1 = sys.stdin.readline().strip()
N = int(s1.split(" ")[0])
D = int(s1.split(" ")[1])

l = []
for i in range(N):
    s2 = sys.stdin.readline().strip()
    li = s2.split(" ")
    l.append([int(i) for i in li])
max_ = 0

i, j = 0, 0
while i < N:
    while j < N:
        if 0 <= i <= N-D and 0 <= j < D-1:
            k = 1
            r = d = rd = l[i][j]
            while k < D:
                r += l[i][j+k]
                d += l[i+k][j]
                rd += l[i+k][j+k]
                k += 1
            if max([r, d, rd])>max_:
                max_ = max([r, d, rd])
        elif 0 <= i <= N-D and D-1 <= j <= N-D:
            k = 1
            r = d = rd = db = l[i][j]
            while k < D:
                r += l[i][j + k]
                d += l[i + k][j]
                rd += l[i + k][j + k]
                db += l[i + k][j - k]
                k += 1
            if max([r, d, rd, db]) > max_:
                max_ = max([r, d, rd, db])
        elif 0 <= i <= N-D and j < N:
            k = 1
            d = db = l[i][j]
            while k < D:
                d += l[i + k][j]
                db += l[i + k][j - k]
                k += 1
            if max([d, db]) > max_:
                max_ = max([d, db])
        elif 0 <= j <= N-D:
            k = 1
            r = l[i][j]
            while k < D:
                r += l[i][j + k]
                k += 1
            if r > max_:
                max_ = r
        j += 1
    i += 1

print(max_)
