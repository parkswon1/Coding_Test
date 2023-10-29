import heapq
import sys

N, M = list(map(int,sys.stdin.readline().split()))

Heap = []

for nm in range(N+M):
    heapq.heappush(Heap, sys.stdin.readline().rstrip())

A = heapq.heappop(Heap)
Output = []
for nm in range(N+M-1):
    B = heapq.heappop(Heap)
    if A == B:
        Output.append(B)
    else:
        A = B

print(len(Output))
for o in Output:
    print(o)