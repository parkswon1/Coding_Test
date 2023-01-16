import sys
N = int(sys.stdin.readline())
miro = []
count = []

for i in range(N):
    miro.append(list(map(int,sys.stdin.readline().split())))
    count.append([0]*N)

count[0][0] = 1

for i in range(N):
    for j in range(N):
        if miro[i][j] == 0:
            break
        y = miro[i][j] + i
        x = miro[i][j] + j
        if y < N:
            count[y][j] += count[i][j]
        if x < N:
            count[i][x] += count[i][j]

print(count[N-1][N-1])