T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = [input().split() for _ in range(N)]

    print(f"#{t}")

    for i in range(N):
        r90 = ""
        r180 = ""
        r270 = ""

        for j in range(N):
            r90 += arr[N - 1 - j][i]
            r180 += arr[N - 1 - i][N - 1 - j]
            r270 += arr[j][N - 1 - i]

        print(r90, r180, r270)