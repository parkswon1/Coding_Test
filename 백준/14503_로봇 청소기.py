def search(x,y):
    global d, count
    if room[y][x] == 0:
        count += 1
        room[y][x] = 2
    check = 0
    for mv in move:
        mx = x + mv[1]
        my = y + mv[0]
        if room[my][mx] == 0:
            check == 1
    if check == 0:
        mx = x - move[d][1]
        my = y - move[d][0]
        if room[my][mx] != 1:
            search(mx,my)
    else:
        for i in range(1, 5):
            d = (d + i)%4
            mx = x + move[d][1]
            my = y + move[d][0]
            if room[my][mx] == 0:
                search(mx,my)

import sys
sys.setrecursionlimit(10**7)

N,M = map(int,sys.stdin.readline().split())
move = [[1,0],[0,1],[-1,0],[0,-1]]
r,c,d = map(int,sys.stdin.readline().split())

room = []
count = 0
for n in range(N):
    room.append(list(map(int,input().split())))
search(c,r)

print(count)