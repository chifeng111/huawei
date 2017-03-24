__author__ = 'zhenhua'
import sys

n = sys.stdin.readline().strip()
n = int(n)
word = []
for i in range(n):
    word.append(sys.stdin.readline().strip())

#print(word)
def check(w1, w2):
    if len(w1) != len(w2):
        return False
    n = len(w1)
    for i in range(n-1):
        w2 = w2[1:] + w2[0]
        if w2 == w1:
            return True
    return False

num = 0
wor = []
for i in range(n-1):
    for j in range(n-i-1):
        if check(word[i], word[i+j+1]):
            if word[i] not in wor and word[i+j+1] not in wor:
                num += 1
            wor.append(word[i])
            wor.append(word[i+j+1])
#print(check('picture', 'turepic'))
print(num)
