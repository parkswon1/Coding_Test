def dfs(n):
    global count, startn
    if visit[n] != 1:
        visit[n] = 1
        dfs(number[n]-1)
        visit[n] = 0
    elif n != startn:
        count += 1

import sys

T = int(sys.stdin.readline())
for t in range(T):
    N = int(sys.stdin.readline())
    number = list(map(int,sys.stdin.readline().split()))
    visit = [0]*N
    count = 0
    for n in range(N):
        startn = n
        visit[n] = 1
        dfs(number[n]-1)
    print(count)