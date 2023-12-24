def DFS():
    global count
    for i in range(N):
        stack = []
        if visit[i] == -1:
            visit[i] = i
            stack.append(i)
        while(stack):
            now = stack.pop()
            next = nodes[now] - 1
            if visit[next] == -1:
                visit[next] = visit[now]
                stack.append(next)
            elif visit[next] == visit[now]:
                count += 1
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    N = int(sys.stdin.readline())
    visit = [-1] * N
    nodes = list(map(int,sys.stdin.readline().split()))
    count = 0
    DFS()
    print(count)