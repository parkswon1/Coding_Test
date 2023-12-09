def melt(node):
    global count, output
    output += 1
    new_node = []
    for n in node:
        visit[n[0]][n[1]] = 0
        for ne in near:
            my = n[0] + ne[0]
            mx = n[1] + ne[1]
            if N > my > -1 and M > mx > -1:
                if board[my][mx] == 0:
                    n[2] -= 1
    for n in node:
        if n[2] <= 0:
            board[n[0]][n[1]] = 0
        else:
            board[n[0]][n[1]] = n[2]
            new_node.append(n)

    if len(new_node) == 0:
        print(0)
        return

    count = 1
    visit[new_node[0][0]][new_node[0][1]] = 1
    count_bing([new_node[0]])

    if count != len(new_node):
        print(output)
        return
    else:
        melt(new_node)

def count_bing(node):
    global count
    new_node = []
    for n in node:
        for ne in near:
            my = n[0] + ne[0]
            mx = n[1] + ne[1]
            if N > my > -1 and M > mx > -1:
                if board[my][mx] != 0 and visit[my][mx] == 0:
                    visit[my][mx] = 1
                    count += 1
                    new_node.append([my,mx])
    if len(new_node) == 0:
        return
    else:
        count_bing(new_node)

import sys
sys.setrecursionlimit(10**7)
N, M = map(int,sys.stdin.readline().split())

board = []
visit = []
node = []
near = [[1,0],[-1,0],[0,1],[0,-1]]
output = 0
for n in range(N):
    line = list(map(int,sys.stdin.readline().split()))
    visit.append([0]*M)
    for m in range(M):
        if line[m] != 0:
            node.append([n,m,line[m]])
    board.append(line)

melt(node)