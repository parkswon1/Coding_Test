def bfs(before):
    after = []
    for b in before:
        y = b[0]
        x = b[1]
        for m in mv:
            my = m[0] + y
            mx = m[1] + x
            if miro[my][mx] == 3:
                print(f'#{test_case}',1)
                return
            elif miro[my][mx] == 0:
                after.append([my,mx])
                miro[y][x] = 1
    if len(after) == 0:
        print(f'#{test_case}',0)
    else:
        bfs(after)

mv = [[1,0],[-1,0],[0,1],[0,-1]]
for test_case in range(1,11):
    input()
    miro = []
    for i in range(16):
        line = [int(i) for i in str(input())]
        miro.append(line)
        for l in range(16):
            if line[l] == 2:
                start = [i,l]
            elif line[l] == 3:
                end = [i,l]
    bfs([start])