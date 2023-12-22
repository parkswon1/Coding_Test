def BFS(prisoner1,prisoner2):
    global doorCount
    newPrisoner1 = []
    newPrisoner2 = []
    out1 = 0
    out2 = 0
    for n in prisoner1:
        if out1 == 1:
            break
        for mv in move:
            my = n[0] + mv[0]
            mx = n[1] + mv[1]
            if H > my > -1 and W > mx > -1:
                if visited1[my][mx] == '#':
                    visited1[my][mx] = visited1[n[0]][n[1]] + 1
                    
                    newPrisoner1.append([my][mx])
                elif visited1[my][mx] == '.':
                    visited1[my][mx] = visited1[n[0]][n[1]]
                    newPrisoner1.append([my][mx])
            else:
                out1 = 1
                doorCount += visited1[n[0]][n[1]]
                break
    for n in prisoner2:
        if out2 == 1:
            break
        for mv in move:
            my = n[0] + mv[0]
            mx = n[1] + mv[1]
            if H > my > -1 and W > mx > -1:
                if visited2[my][mx] == '#':
                    visited2[my][mx] = visited2[n[0]][n[1]] + 1
                elif visited2[my][mx] == '.':
                    visited2[my][mx] = visited2[n[0]][n[1]]
                    newPrisoner2.append([my][mx])
            else:
                out2 = 1
                doorCount += visited2[n[0]][n[1]]
                break

import sys

T = int(sys.stdin.readline())
move = [[1,0],[-1,0],[0,1],[0,-1]]
for t in range(T):
    H,W = map(int,sys.stdin.readline().split())
    visited1 = []
    visited2 = []
    prisoner1 = []
    prisoner2 = []
    check = 1
    for h in range(H):
        line = list(map(int,sys.stdin.readline().split()))
        for w in range(W):
            if line[w] == '$':
                if check == 1:
                    prisoner1.append([h,w])
                    check = 2
                else:
                    prisoner2.append([h,w])
        visited1.append(line)
        visited2.append(line)
    doorCount = 0
    BFS(prisoner1,prisoner2)