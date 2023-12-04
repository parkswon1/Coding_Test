def spin(N,D):
    if D == 1:
        gears[N].appendleft(gears[N].pop())
    else:
        gears[N].append(gears[N].popleft())

import sys
from collections import deque

gears = []
for _ in range(4):
    gears.append(deque([int(i) for i in sys.stdin.readline().rstrip()]))

K = int(input())

for k in range(K):
    N,D = map(int,sys.stdin.readline().split())
    N -= 1
    left = gears[N][6]
    right = gears[N][2]
    spin(N,D)
    d = -D
    for n in range(N+1,4):
        rightleft = gears[n][6]
        newright = gears[n][2]
        if rightleft != right:
            spin(n,d)
            d = -d
            right = newright
        else:
            break
    d = -D
    for n in range(N-1,-1,-1):
        leftright = gears[n][2]
        newleft = gears[n][6]
        if leftright != left:
            spin(n,d)
            d = -d
            left = newleft
        else:
            break

output = 0
score = [1,2,4,8]
for i in range(4):
    if gears[i][0] == 1:
        output += score[i]

print(output)