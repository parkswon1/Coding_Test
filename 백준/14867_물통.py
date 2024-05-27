from collections import deque

a, b, c, d = map(int, input().split())

visited = set()
queue = deque([])
goal = (c, d)
queue.append((0, 0, 0))
visited.add((0,0))

def bfs():
    while queue:
        A, B, count = queue.popleft()

        if (A, B) == goal:
            print(count)
            return

        if (a, B) not in visited:
            visited.add((a, B))
            queue.append((a, B, count + 1))

        if (A, b) not in visited:
            visited.add((A, b))
            queue.append((A, b, count + 1))

        if (0, B) not in visited:
            visited.add((0, B))
            queue.append((0, B, count + 1))

        if (A, 0) not in visited:
            visited.add((A, 0))
            queue.append((A, 0, count + 1))

        AtoB = min(A + B, b)
        nextA = A - (AtoB - B)
        if (nextA, AtoB) not in visited:
            visited.add((nextA, AtoB))
            queue.append((nextA, AtoB, count + 1))

        BtoA = min(A + B, a)
        nextB = B - (BtoA - A)
        if (BtoA, nextB) not in visited:
            visited.add((BtoA, nextB))
            queue.append((BtoA, nextB, count + 1))

    print(-1)

bfs()
