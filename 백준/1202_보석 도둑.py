import sys
import heapq

N, K = map(int,sys.stdin.readline().split())
heap = []
for n in range(N):
    M,V = map(int,sys.stdin.readline().split())
    heapq.heappush(heap,[M,V])

bag = []
for k in range(K):
    bag.append(int(sys.stdin.readline()))
bag.sort()
Gems = []
output = 0

for b in bag:
    while heap and heap[0][0] <= b:
        heapq.heappush(Gems,-heap[0][1])
        heapq.heappop(heap)
    if Gems:
        output -= heapq.heappop(Gems)
print(output)