import heapq
import sys
N = int(sys.stdin.readline())

if N == 1:
    print(int(sys.stdin.readline()))
else:
    Heap = []
    for n in range(N):
        heapq.heappush(Heap, int(sys.stdin.readline()))

    Output = 0
    for n in range(N-1):
        Sum = heapq.heappop(Heap) + heapq.heappop(Heap)
        Output += Sum
        heapq.heappush(Heap, Sum)
    
    print(Output)