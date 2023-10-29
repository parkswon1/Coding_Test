import heapq
import sys
N = int(sys.stdin.readline())

time = []
for i in range(N):
    time.append(list(map(int,sys.stdin.readline().split())))

time.sort()

room = [time[0][1]]

for i in range(1,N):
    if time[i][0] >= room[0]:
        heapq.heappop(room)
    heapq.heappush(room, time[i][1])
        
print(len(room))