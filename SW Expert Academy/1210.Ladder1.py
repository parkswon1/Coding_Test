def dfs(start):
    y = start[0]
    x = start[1]
    for lr in left_right:
        mx = x + lr
        if 100 > mx > -1 and ladder[y][mx] == 1:
            ladder[y][x] = 0
            dfs([y,mx])
            return
    my = y - 1
    if my == 0:
        print(f'#{test_case}', x)
    else:
        dfs([my,x])

left_right = [1,-1]
for test_case in range(1,11):
    input()
    ladder = []

    for i in range(100):
        ladder.append(list(map(int,input().split())))

    start_point = ladder[99].index(2)
    start = [99,start_point]

    dfs(start)