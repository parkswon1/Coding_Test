from collections import deque

def solution(maps):
    N = len(maps[0])
    M = len(maps)
    move = [[1,0],[0,1],[-1,0],[0,-1]]
    maps[0][0] = 0
    que = deque([[0,0,1]])

    while(que):
        y,x,z = que.popleft()
        for mv in move:
            my = mv[0] + y
            mx = mv[1] + x
            mz = z + 1
            if 0 <= my < M and 0 <= mx < N:
                if my == M - 1 and mx == N - 1:
                    return mz
                elif maps[my][mx] == 1:
                    maps[my][mx] = 0
                    que.append([my,mx,mz])

    return -1

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))