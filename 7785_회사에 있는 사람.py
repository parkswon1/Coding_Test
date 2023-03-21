import heapq

import sys
n = int(sys.stdin.readline())

Heap = []

for nm in range(n):
    Input = list(sys.stdin.readline().split())
    heapq.heappush(Heap, Input[0])

A = heapq.heappop(Heap)
Output = []
for n in range(n-1):
    B = heapq.heappop(Heap)
    if A != B:
        Output.append(A)
        A = B

if B != Output[-1]:
    Output.append(B)

for o in range(-1,-len(Output)-1,-1):
    print(Output[o])