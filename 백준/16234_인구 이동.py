from collections import deque
import sys

board = []
N, L, R = map(int, sys.stdin.readline().split())
for n in range(1, N + 1):
    board.append(list(map(int, sys.stdin.readline().split())))

move = [(0,1),(0,-1),(1,0),(-1,0)]
def search():
    day = 0
    global board
    while(1):
        check = 0
        visited = set()
        for y in range(N):
            for x in range(N):
                if (y, x) not in visited:
                    nodes = deque([(y, x)])
                    visited.add((y, x))
                    totalPeople = board[y][x]
                    totalCountry = set()
                    totalCountry.add((y, x))
                    while nodes:
                        node = nodes.popleft()
                        for mv in move:
                            my, mx = node[0] + mv[0], node[1] + mv[1]

                            if ((my, mx) not in visited and 0 <= my < N and 0 <= mx < N
                                    and L <= abs(board[node[0]][node[1]] - board[my][mx]) <= R):
                                check = 1
                                visited.add((my, mx))
                                totalCountry.add((my, mx))
                                totalPeople += board[my][mx]
                                nodes.append((my, mx))

                    nextPeople = totalPeople // len(totalCountry)
                    for v in totalCountry:
                        board[v[0]][v[1]] = nextPeople

        if check == 0:
            return day
        else:
            day += 1

print(search())