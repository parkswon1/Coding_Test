from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
i = 1
visit = [-1]*500001
visit[N] = 0

queue = deque([N])
while queue:
    current = queue.popleft()

    if K + visit[current] > 500000:
        print(-1)
        break
    elif current == K + visit[current]:
        print(visit[K])
        break

    n_next = current * 2
    if n_next < 500001 and visit[n_next] == -1 and n_next != 0:
        visit[n_next] = visit[current] + 1
        queue.append(n_next)
    n_next = current - 1
    if 0 <= n_next < 500001 and visit[n_next] == -1:
        visit[n_next] = visit[current] + 1
        queue.append(n_next)
    n_next = current + 1
    if n_next < 500001 and visit[n_next] == -1:
        visit[n_next] = visit[current] + 1
        queue.append(n_next)

