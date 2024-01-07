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
    line1 = [0] * M
    line2 = [0] * M
    line1[0] = count[i - 1][0] + miro[i][0]
    for j in range(1,M):
        line1[j] = miro[i][j] + max(count[i-1][j], line1[j - 1])

    line2[-1] = count[i - 1][-1] + miro[i][-1]
    for j in range(M - 2, -1, -1):
        line2[j] = miro[i][j] + max(count[i-1][j], line2[j + 1])

    for j in range(M):
        count[i][j] = max(line1[j], line2[j])

print(count[N-1][M-1])