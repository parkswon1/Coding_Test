def search(x):
    global output
    distance[x] = 0
    for _ in range(N):
        low_distance = 99999999999999999
        low_dis_index = -1
        for v in range(N):
            if visited[v] == 0:
                if distance[v] < low_distance:
                    low_distance = distance[v]
                    low_dis_index = v

        visited[low_dis_index] = 1
        output += E*low_distance
        for j in range(N):
            if visited[j] == 0:
                distance[j] = min(distance[j], (X[low_dis_index] - X[j]) ** 2 + (Y[low_dis_index] - Y[j]) ** 2)

T = int(input())

for test_case in range(1,T+1):
    output = 0
    N = int(input())
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    E = float(input())

    visited = [0]*N
    distance = [1500000]*N
    search(0)
    print(f'#{test_case}',int(output))