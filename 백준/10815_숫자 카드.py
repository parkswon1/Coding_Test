import sys
N = int(sys.stdin.readline())
Plist = [0]*10000001
Mlist = [0]*10000001
numbers = list(map(int,sys.stdin.readline().split()))
zero = 0
for i in numbers:
    if i <0:
        Mlist[i] =i
    elif i == 0:
        zero = 1
    else:
        Plist[i] =i
answer = []
M = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
for j in numbers:
    check = 0
    if j == 0:
        if zero == 1:
            check = 1
            answer.append(1)
    elif j > 0:
        if Plist[j] != 0:
            check = 1
            answer.append(1)
    else:      
        if Mlist[j] != 0 :
            check = 1
            answer.append(1)
    if check == 0:
        answer.append(0)

print(*answer)