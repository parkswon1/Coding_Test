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

for c in range(ccount):
    search(cuntinent[c])