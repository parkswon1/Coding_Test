import sys
N, M = list(map(int, sys.stdin.readline().split()))
miro = []
count = []

for i in range(N):
    miro.append(list(map(int,sys.stdin.readline().split())))
    count.append([0]*M)

count[0][0] = 1

for i in range(M):
    if i != M-1:
        if miro[0][i] > miro[0][i+1]:
            count[0][i+1] += count[0][i]
        if miro[0][i] > miro[1][i]:
            count[1][i] += count[0][i]
    else:
        if miro[0][i] > miro[1][i]:
            count[1][i] += count[0][i]

for y in range(1,N-1):
    for x in range(M-1):
        if miro[y][x] > miro[y][x+1]:
            count[y][x+1] += count[y][x]

        a = -x-1
        
        if miro[y][a] > miro[y][a-1]:
            count[y][a-1] += count[y][a]
    
    for x in range(M):
        if miro[y][x] > miro[y+1][x]:
            count[y+1][x] += count[y][x]

for i in range(M-1):
    if miro[-1][i] > miro[-1][i+1]:
        count[-1][i+1] += count[-1][i]

print(count[N-1][M-1])