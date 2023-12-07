import sys
from itertools import combinations

def mark(node):
    global count
    newnode = []
    for n in node:
        for m in move:
            my = n[0] + m[0]
            mx = n[1] + m[1]
            if N > my > -1 and N > mx > -1:
                if board[my][mx] == 1:
                    board[my][mx] = count
                    continent[ccount].append([my, mx])
                    newnode.append([my, mx])
    if len(newnode) > 0:
        mark(newnode)

def calculate_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

sys.setrecursionlimit(10**7)

continent = []
board = []
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
N = int(sys.stdin.readline())

for n in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

count = 1
ccount = 0
for n in range(N):
    for m in range(N):
        if board[n][m] == 1:
            continent.append([])
            count += 1
            board[n][m] = count
            continent[ccount].append([n, m])
            mark([[n, m]])
            ccount += 1

min_distance = float('inf')
for pair in combinations(range(len(continent)), 2):
    for coord1 in continent[pair[0]]:
        for coord2 in continent[pair[1]]:
            min_distance = min(min_distance, calculate_distance(coord1, coord2))

print(min_distance - 1)