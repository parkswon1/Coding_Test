import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def isTree(startNode):
    queue = deque([startNode])
    parent[startNode] = -1
    edgeCount = 0
    nodeCount = 0

    while queue:
        node = queue.popleft()
        nodeCount += 1
        for neighbor in graph[node]:
            if neighbor == parent[node]:
                continue
            if visited[neighbor]:
                return False
            visited[neighbor] = True
            parent[neighbor] = node
            queue.append(neighbor)
            edgeCount += 1

    return edgeCount == nodeCount - 1

caseNumber = 1

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    graph = defaultdict(list)
    parent = [-1] * (n + 1)
    visited = [False] * (n + 1)
    treeCount = 0

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for node in range(1, n + 1):
        if not visited[node]:
            visited[node] = True
            if isTree(node):
                treeCount += 1

    if treeCount == 0:
        print(f'Case {caseNumber}: No trees.')
    elif treeCount == 1:
        print(f'Case {caseNumber}: There is one tree.')
    else:
        print(f'Case {caseNumber}: A forest of {treeCount} trees.')

    caseNumber += 1