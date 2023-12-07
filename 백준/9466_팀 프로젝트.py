def dfs(n):
    global count
    if visit[n] != 1:
        team.append(n)
        visit[n] = 1
        dfs(number[n]-1)
    else:
        I = len(team)
        for i in range(I):
            if team[i] == n:
                count += (I - i)

import sys
sys.setrecursionlimit(10**7)
T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    number = list(map(int,sys.stdin.readline().split()))
    visit = [0]*N
    count = 0
    for n in range(N):
        if visit[n] != 1:
            team = [n]
            visit[n] = 1
            dfs(number[n]-1)
    print(N - count)