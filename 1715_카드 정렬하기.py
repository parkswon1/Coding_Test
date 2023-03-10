import heapq
import sys
N = int(sys.stdin.readline())

if N == 1:
    print(int(sys.stdin.readline()))
else:
    Heap = []
    for n in range(N):
        heapq.heappush(Heap, int(sys.stdin.readline()))

    Output = heapq.heappop(Heap) + heapq.heappop(Heap)
    for n in range(N-2):
        Output = Output*2 + heapq.heappop(Heap)
    
    print(Output)