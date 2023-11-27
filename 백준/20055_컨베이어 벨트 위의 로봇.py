from collections import deque
import sys
N, K = map(int,sys.stdin.readline().split())
A = deque(list(map(int,sys.stdin.readline().split())))
count = 0
stage = 0
robots = [0]*N
while count < K:
    A.appendleft(A.pop())
    for n in range(N - 2, -1, -1):
        if robots[n] == 1:
            robots[n] = 0
            robots[n + 1] = 1
    robots[N - 1] = 0
    for n in range(N - 2, -1, -1):
        if robots[n] == 1 and robots[n + 1] == 0 and A[n + 1] != 0:
            robots[n] = 0
            robots[n + 1] = 1
            A[n + 1] -= 1
            if A[n + 1] == 0:
                count += 1
    robots[N - 1] = 0

    if A[0] != 0:
        A[0] -= 1
        robots[0] = 1
        if A[0] == 0:
            count += 1
    stage += 1

print(stage)