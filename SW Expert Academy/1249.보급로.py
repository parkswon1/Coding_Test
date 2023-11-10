def dfs(y,x):
    for m in move:
        mx = x + m[1]
        my = y + m[0]
        if N > mx > -1 and N > my > -1:
            score = score_map[y][x] + n_map[my][mx]
            if score < score_map[my][mx]:
                score_map[my][mx] = score
                
                if mx == N -1 and my == N-1:
                    return
                else:
                    dfs(my,mx)

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    n_map = []
    score_map = []
    move = [[1,0],[-1,0],[0,1],[0,-1]]
    for n in range(N):
        score_map.append([999999999]*N)
        n_map.append([int(l) for l in str(input())])
    
    score_map[0][0] = 0
    dfs(0,0)
    
    print(f"#{test_case}", score_map[N-1][N-1])