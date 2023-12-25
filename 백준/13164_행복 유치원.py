import sys
import heapq

N, K = list(map(int,sys.stdin.readline().split()))
tail = list(map(int,sys.stdin.readline().split()))
heap = []
for i in range(1,N):
    diff = tail[i] - tail[i-1]
    heapq.heappush(heap,diff)

output = 0
for j in range(N-K):
    output += heapq.heappop(heap)

print(output)