#coding:utf-8
import sys
def test(input_):
    first_line = input_
    N = int(first_line.split(" ")[0])
    M = int(first_line.split(" ")[1])
    student = [0]
    second_line = sys.stdin.readline().strip()
    for i in range(N):
        student.append(int(second_line.split(" ")[i]))

    for i in range(M):
        key = sys.stdin.readline().strip()
        C = key.split(" ")[0]
        A = int(key.split(" ")[1])
        B = int(key.split(" ")[2])
        if C == 'Q':
            if A > B:
                A,B=B,A
            print(max(student[A:B+1]))
        else:
            student[A] = B

try:
    while 1:
        input_ = sys.stdin.readline().strip()
        if input_ == "":
            break
        test(input_)

except:
    pass