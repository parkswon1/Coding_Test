import sys

N = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
output = [0]*N

right = []

for n in range(N-1,-1,-1):
    now = numbers[n]
    while(right):
        if right[-1] <= now:
            right.pop()
        else:
            break
    if len(right) == 0:
        output[n] = -1
    else:
        output[n] = right[-1]
    right.append(now)

print(*output)