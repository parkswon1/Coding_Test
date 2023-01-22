def dfs(i,j):
    global count
    for yx in move:
        x = j + yx[1]
        y = i + yx[0]
        if 0 <= y < N and 0 <= x < N:
           if apert[y][x] == '1':
               apert[y][x] = apt
               count += 1
               dfs(y,x)

import sys
N = int(sys.stdin.readline())
move = [[0,1],[0,-1],[1,0],[-1,0]]

apert = []
for i in range(N):
    apert.append(list(sys.stdin.readline().rstrip()))

apt = 0
output = []
count = 1
for i in range(N):
    for j in range(N):
        if apert[i][j] == '1':
            apert[i][j] = apt
            apt += 1
            dfs(i,j)
            output.append(count)
            count = 1
            
print(apt)
output.sort()
for i in output:
    print(i)