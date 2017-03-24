import sys

def new_str(s):
    n = len(s)
    if n == 1:
        return '1' + s
    letter = []
    num = []
    i = 0
    while i < n:
        if i == 0:
            letter.append(s[0])
            count = 1
        elif i == n-1:
            if s[i] == s[i-1]:
                num.append(count+1)
            else:
                num.append(count)
                letter.append(s[i])
                num.append(1)
        else:
            if s[i] == s[i-1]:
                count += 1
            else:
                num.append(count)
                letter.append(s[i])
                count = 1
        i += 1
    str_ = []
    for x, y in zip(num, letter):
        str_.append(str(x)+y)
    return ''.join(str_)



s = sys.stdin.readline().strip()

print(new_str(s))
