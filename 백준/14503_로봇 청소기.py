def search(y,x):
    global d,count
    if room[y][x] == 0:
        room[y][x] = 2
        count += 1
    check = 0
    for i in range(1,5):
        d = (d + 1)%4
        my = move[d][0] + y
        mx = move[d][1] + x
        if room[my][mx] == 0:
            check = 1
            break
    if check == 0:
        my = y - move[d][0]
        mx = x - move[d][1]
        if room[my][mx] == 1:
            return
    search(my,mx)

import sys
sys.setrecursionlimit(10**7)
move = [[-1,0],[0,-1],[1,0],[0,1]]
N, M = map(int,sys.stdin.readline().split())
r,c,d = map(int,sys.stdin.readline().split())
if d == 1 or d == 3:
    d = (d+2)%4
room = []
for n in range(N):
    room.append(list(map(int,sys.stdin.readline().split())))
count = 0
search(r,c)
print(count)