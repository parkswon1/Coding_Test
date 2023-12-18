import sys
from collections import deque

N, C = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())

sendingInfo = []
for m in range(M):
    sendingInfo.append(list(map(int,sys.stdin.readline().split())))

sendingInfo.sort()
sendingInfo = deque(sendingInfo)

cargo = deque([])
maxC = 0

output = 0

for n in range(1,N+1):
    while(cargo):
        if cargo[0][0] == n:
            maxC -= cargo[0][1]
        cargo.popleft()
            
    while(sendingInfo):
        if sendingInfo[0][0] == n:
            if maxC != C:
                maxC += sendingInfo[0][2]
                diff = maxC - C
                if diff > 0:
                    maxC = C
                    sendingInfo[0][2] -= diff
                cargo.append([sendingInfo[0][1],sendingInfo[0][2]])
            sendingInfo.popleft()