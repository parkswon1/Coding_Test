import sys, copy
from collections import deque

def wakeVirus(index):
    global count,output
    for i in range(index,virusCount):
        nowVirus.append(virus[i] + [0])
        if len(nowVirus) == M:
            virusList = copy.deepcopy(nowVirus)
            copyBoard = copy.deepcopy(board)
            bfs(virusList,copyBoard)
        else:
            wakeVirus(i+1)
        nowVirus.pop()
    return

def bfs(virusList,copyBoard):
    global output
    time = 0
    zeroCount = 0
    if zeroCount == cleanCount:
        output = 0
        return
    while(virusList):
        y,x,c = virusList.popleft()
        time = max(time,c)
        for mv in move:
            my = y + mv[0]
            mx = x + mv[1]
            if 0 <= my < N and 0 <= mx < N:
                if copyBoard[my][mx] != 1:
                    if copyBoard[my][mx] == 0:
                        zeroCount += 1
                        if zeroCount == cleanCount:
                            output = min(c+1, output)
                            return
                    copyBoard[my][mx] = 1
                    virusList.append([my,mx,c+1])

N, M = map(int, sys.stdin.readline().split())
board = []
virus = []
move = [[1,0],[0,1],[-1,0],[0,-1]]
cleanCount = 0
for n in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    for m in range(N):
        if line[m] == 2:
            virus.append([n,m])
        if line[m] == 0:
            cleanCount +=1
    board.append(line)

virusCount = len(virus)
nowVirus = deque([])
output = float('inf')
wakeVirus(0)

if output != float('inf'):
    print(output)
else:
    print(-1)