def dfs(y,x,mv):
    global count
    snail[y][x] = count
    if count == N*N:
        return
    my = mv[0] + y
    mx = mv[1] + x
    if N > my > -1 and N > mx > -1 and snail[my][mx] == 0:
        count += 1
        dfs(my,mx,mv)
    else:
        if mv == [0,1]:
            mv = [1,0]
            dfs(y, x, mv)
        elif mv == [0,-1]:
            mv = [-1, 0]
            dfs(y, x, mv)
        elif mv == [1,0]:
            mv = [0, -1]
            dfs(y, x, mv)
        elif mv == [-1,0]:
            mv = [0, 1]
            dfs(y, x, mv)

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    snail = []
    count = 1
    for n in range(N):
        snail.append([0]*N)

    dfs(0,0,[0,1])

    print(f'#{test_case}')
    for n in range(N):
        print(*snail[n])