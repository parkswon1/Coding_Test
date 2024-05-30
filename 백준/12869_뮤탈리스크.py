import itertools
from collections import deque

N = int(input())
SCVS = tuple(list(map(int, input().split())) + [0])
move = list(itertools.permutations([1,3,9]))
visited = set([])

count = float('inf')
queue = deque([SCVS])
visited.add(SCVS[0:N])
last = tuple([0] * N)
if SCVS[0:N] == [0,0,0]:
    print(0)
else:
    while (queue):
        node = queue.popleft()
        for mv in move:
            nextNode = [0] * N + [node[N] + 1]
            for i in range(N):
                nextNode[i] = max(0, node[i] - mv[i])
            tupleNode = tuple(nextNode)
            if node[:N] == last:
                count = min(node[N], count)
            elif tupleNode[:N] not in visited:
                queue.append(tupleNode)
                visited.add(tupleNode[:N])

print(count)