import sys
import heapq

N = int(sys.stdin.readline())

heap = []

for i in range(N):
    heapq.heappush(heap,list(map(int,sys.stdin.readline().split())))

output = 0
room = [-1]
for i in range(N):
    start,end = heapq.heappop(heap)
    while(room):
        if start >= room[0]:
            heapq.heappop(room)
        else:
            break
    heapq.heappush(room,end)
    output = max(len(room), output)

print(output)