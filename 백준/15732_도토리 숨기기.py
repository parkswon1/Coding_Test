import sys

N, K, D = map(int, sys.stdin.readline().split())

rules = []
for k in range(K):
    rules.append(list(map(int, sys.stdin.readline().split())))

front = 1
back = N
answer = 0
while(front <= back):
    mid = (front + back) // 2
    count = 0
    for A, B, C in rules:
        if (A <= mid):
            count += ((min(mid, B) - A)//C) + 1

    if count < D:
        front = mid + 1
    else:
        answer = mid
        back = mid - 1

print(answer)