def bfs(ice):
    global year,count
    year += 1
    new_ice = []
    ice_count = len(ice)
    minus = [0] * ice_count
    for _ in range(ice_count):
        i = ice[_]
        visit[i[0]][i[1]] = 0
        for s in surround:
            mx = i[1] + s[1]
            my = i[0] + s[0]
            if N > my > -1 and M > mx > -1:
                if board[my][mx] == 0:
                    minus[_] += 1

    for k in range(ice_count):
        x = ice[k][1]
        y = ice[k][0]
        board[y][x] -= minus[k]
        if board[y][x] > 0:
            new_ice.append([y,x])
        else:
            board[y][x] = 0
    visit[new_ice[0][0]][new_ice[0][1]] = 1
    count = 1
    search([[new_ice[1][0],new_ice[1][1]]])

    if count < len(new_ice):
        print(year)
        return
    if len(new_ice) == 0:
        print(0)
        return
    else:
        bfs(new_ice)

def search(bings):
    global count
    new_bings = []
    for b in bings:
        for s in surround:
            my = b[0] + s[0]
            mx = b[1] + s[1]
            if N > my > -1 and M > mx > -1:
                if visit[my][mx] == 0:
                    count += 1
                    visit[my][mx] = 1
                    new_bings.append([my,mx])
    if len(new_bings) == 0:
        return
    else:
        search(new_bings)


import sys
sys.setrecursionlimit(10**7)

surround = [[1,0],[-1,0],[0,1],[0,-1]]
N, M = map(int,sys.stdin.readline().split())
board = []
ice = []
visit = []
year = 0
count = 1
for n in range(N):
    visit.append([0]*M)
    line = list(map(int,sys.stdin.readline().split()))
    for m in range(M):
        if line[m] != 0:
            ice.append([n,m])
    board.append(line)

bfs(ice)