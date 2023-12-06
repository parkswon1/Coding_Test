def bfs(S):
    global minutes
    minutes += 1
    newS = []
    for s in S:
        for m in move:
            mz = m[0] + s[0]
            my = m[1] + s[1]
            mx = m[2] + s[2]
            if L > mz > -1 and R > my > -1 and C > mx > -1:
                if bilding[mz][my][mx] == 'E':
                    print(f'Escaped in {minutes} minute(s).')
                    return
                if bilding[mz][my][mx] == '.':
                    bilding[mz][my][mx] = 'S'
                    newS.append([mz,my,mx])
    if len(newS) == 0:
        print('Trapped!')
    else:
        bfs(newS)

import sys
sys.setrecursionlimit(10**7)

while(1):
    L,R,C = map(int,sys.stdin.readline().split())
    if [L,R,C] == [0,0,0]:
        break
    bilding = []
    move = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,-1],[0,0,1]]
    for l in range(L):
        floor = []
        for r in range(R):
            line = list(sys.stdin.readline().rstrip())
            for c in range(C):
                if line[c] == 'S':
                    S = [[l,r,c]]
            floor.append(line)
        bilding.append(floor)
        sys.stdin.readline()
    minutes = 0
    bfs(S)