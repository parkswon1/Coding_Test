import sys
sys.setrecursionlimit(10**6)

N, M = list(map(int,sys.stdin.readline().split()))
miro = []
count = []
for i in range(N):
    miro.append(list(map(int,sys.stdin.readline().split())))
    count.append([0]*M)

count[0][0] = miro[0][0]
for i in range(1,M):
    count[0][i] = miro[0][i]+count[0][i-1]

for i in range(1,N):
    for j in range(M):
        count[i][j] = miro[i][j] + max(count[i-1][j], count[i][j-1])

print(count[N-1][M-1])