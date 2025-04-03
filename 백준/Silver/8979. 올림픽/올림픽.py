import sys

N, K = map(int, sys.stdin.readline().split())
country = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

country.sort(key=lambda x: (-x[1], -x[2], -x[3]))

for i in range(N):
    if country[i][0] == K:
        if i == 0:
            print(1)
            break
        else:
            for n in range(i - 1, -1, -1):
                if country[n][1:] != country[i][1:]:
                    print(n + 2)
                    break
            else:
                print(1)