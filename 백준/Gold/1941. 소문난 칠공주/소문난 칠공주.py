from itertools import combinations
from collections import deque

board = [list(input().strip()) for _ in range(5)]

positions = [(i // 5, i % 5) for i in range(25)]

result = 0

def is_connected(selected):
    queue = deque([selected[0]])
    visited = set([selected[0]])

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in selected and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    return len(visited) == 7

for comb in combinations(positions, 7):
    s_count = sum(1 for x, y in comb if board[x][y] == 'S')
    if s_count >= 4 and is_connected(comb):
        result += 1

print(result)