import heapq
import sys
N = int(sys.stdin.readline())
 
heap = []
for i in range(N):
    infromation = int(sys.stdin.readline())
    if infromation == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,infromation)