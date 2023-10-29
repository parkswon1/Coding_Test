import sys

def bfs(S,water,count):
    nextS = []
    nextwater = []
    for w in water:
        for mv in move:
            x = w[1] + mv[1]
            y = w[0] + mv[0]
            if 0 <= x < C and 0 <= y < R:
                if jido[y][x] == '.':
                    jido[y][x] = count
                    nextwater.append([y,x])
    for s in S:
        for mv in move:
            x = s[1] + mv[1]
            y = s[0] + mv[0]
            if 0 <= x < C and 0 <= y < R:
                if [y,x] == D:
                    print(count)
                    return
                if jido[y][x] == '.':
                    jido[y][x] = 0
                    nextS.append([y,x])
    if len(nextS) == 0:
        print("KAKTUS")
    else:
        bfs(nextS,nextwater,count+1)
            
R, C = list(map(int,sys.stdin.readline().split()))

jido = []
water = []
move = [[0,1],[0,-1],[1,0],[-1,0]]

for i in range(R):
    line = list(sys.stdin.readline().rstrip())
    for j in range(C):
        if line[j] == 'D':
            D = [i,j]
        elif line[j] == 'S':
            S = [[i,j]]
        elif line[j] == '*':
            water.append([i,j])
    jido.append(line)

bfs(S,water,1)