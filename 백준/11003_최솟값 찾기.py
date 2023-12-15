import sys
from collections import deque

N, L = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))

queue = deque()
for i in range(N):
    while(queue):
        if queue[-1][1] > A[i]:
            queue.pop()
        else:
            break
    if queue and i - queue[0][0] >= L:
        queue.popleft()
    queue.append((i,A[i]))
    print(queue[0][1], end=' ')