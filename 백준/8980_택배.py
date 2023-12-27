import sys
import heapq
N, C = map(int,sys.stdin.readline().split())
M = int(sys.stdin.readline())
sendingBox = []
for m in range(M):
    heapq.heappush(sendingBox,list(map(int,sys.stdin.readline().split())))

cargo = [0]*(N + 1)
lastindex = 0
totalCargo = 0

output = 0
for n in range(1,N+1):
    output += cargo[n]
    totalCargo -= cargo[n]

    while(sendingBox):
        if sendingBox[0][0] == n: ##보내는 마을에 도착한 상자라면
            box = heapq.heappop(sendingBox) ##일단 상자 넣기
            lastindex = max(box[1],lastindex)
            cargo[box[1]] += box[2]
            totalCargo += box[2]
            diff = totalCargo - C
            if diff > 0:
                totalCargo = C
            while diff > 0: ##만약 상자 넣었는데 최대 용량 초과라면 초과량 만큼 가장 늦게 주는 마을 상자부터 하차 !!
                if cargo[lastindex] >= diff:
                    cargo[lastindex] -= diff
                    diff = 0
                    break
                else:
                    diff -= cargo[lastindex]
                    cargo[lastindex] = 0
                    while lastindex > 0: ##lastindex앞으로 움직이기
                        lastindex -= 1
                        if cargo[lastindex] != 0:
                            break
        else:
            break


print(output)