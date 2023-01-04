import sys
N = int(sys.stdin.readline())
minus =[0]*10000001
plus = [0]*10000001
number = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
for i in number:
    if i < 0:
        minus[i] += 1
    else:
        plus[i] += 1
output = []
for i in numbers:
    if i < 0:
        output.append(minus[i])
    else:
        output.append(plus[i])
print(*output)
