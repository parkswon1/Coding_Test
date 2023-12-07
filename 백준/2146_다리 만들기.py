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
                    cuntinent[ccount].append([my,mx])
                    newnode.append([my,mx])
    if len(newnode) > 0:
        mark(newnode)

def search(node):
    global count, distance
    count += 1
    newnode = []
    for n in node:
        for m in move:
            my = n[0] + m[0]
            mx = n[1] + m[1]
            if N > my > -1 and N > mx > -1:
                if board[my][mx] == sea:
                    board[my][mx] = now_n
                    newnode.append([my,mx])
                elif board[my][mx] != now_n:
                    distance = min(distance,count)

    if len(newnode) > 0:
        search(newnode)

import sys
sys.setrecursionlimit(10**7)

cuntinent = []
board = []
move = [[1,0],[-1,0],[0,1],[0,-1]]
N = int(sys.stdin.readline())

for n in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

count = 1
ccount = 0
for n in range(N):
    for m in range(N):
        if board[n][m] == 1:
            cuntinent.append([])
            count += 1
            board[n][m] = count
            cuntinent[ccount].append([n,m])
            mark([[n,m]])
            ccount += 1

sea = 0
distance = float('inf')
for i in range(len(cuntinent)-1):
    now_n = board[cuntinent[i][0][0]][cuntinent[i][0][1]]
    count = 0
    search(cuntinent[i])
    sea = now_n

print(distance-1)