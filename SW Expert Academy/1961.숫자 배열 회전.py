T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int,input().split())))
    first = []
    second = []
    thrid = []

    for x in range(N):
        line = []
        for y in range(N-1,-1,-1):
            line.append(matrix[y][x])
        first.append(''.join(map(str,line)))

    for y in range(N-1,-1,-1):
        line = []
        for x in range(N-1,-1,-1):
            line.append(matrix[y][x])
        second.append(''.join(map(str,line)))

    for x in range(N-1,-1,-1):
        line = []
        for y in range(N):
            line.append(matrix[y][x])
        thrid.append(''.join(map(str,line)))

    print(f'#{test_case}')
    for i in range(len(first)):
        print(first[i],second[i],thrid[i])