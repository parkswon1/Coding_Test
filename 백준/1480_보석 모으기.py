def solve(bag, weight, visited):
    if bag == M:
        return -1
    if visited == (1 << N) - 1:
        return 0

    if cache[bag][weight][visited] != -1:
        return cache[bag][weight][visited]

    ret = 0
    for i in range(N):
        if visited & (1 << i):
            continue
        elif arr[i] > C:
            continue
        elif weight + arr[i] > C:
            ret = max(ret, solve(bag + 1, arr[i], visited | (1 << i)) + 1)
        else:
            ret = max(ret, solve(bag, weight + arr[i], visited | (1 << i)) + 1)

    cache[bag][weight][visited] = ret
    return ret

N, M, C = map(int, input().split())
arr = list(map(int, input().split()))
cache = [[[-1 for _ in range(1 << 13)] for _ in range(21)] for _ in range(11)]

print(solve(0, 0, 0))

# q, M, C = map(int, input().split())
# C += 1
# jewels = list(map(int, input().split()))
# jewels.sort()
# bag = 0
# output = 0
#
# def DynamicPrograming(jewels):
#     global bag, output
#     N = len(jewels)
#     if bag == M:
#         print(output)
#         return
#     dp = []
#     for n in range(N + 1):
#         dp.append([[] for i in range(C)])
#
#     for y in range(1, N + 1):
#         for x in range(C):
#             nowlist = []
#             if x >= jewels[y - 1]:
#                 nowlist = nowlist + dp[y - 1][x - jewels[y - 1]]
#                 nowlist.append(jewels[y - 1])
#
#             if len(nowlist) >= len(dp[y - 1][x]):
#                 dp[y][x] = dp[y][x] + nowlist
#             else:
#                 dp[y][x] = dp[y][x] + dp[y - 1][x]
#     bag += 1
#     output += len(dp[N][C - 1])
#     for rm in dp[N][C - 1]:
#         jewels.remove(rm)
#     DynamicPrograming(jewels)
#
# DynamicPrograming(jewels)
#
# 반례
# 8 3 10
# 1 2 3 4 5 6 7 8
#
# 한가방에 최대로 담을 수 있을때 무조건 최대 개수로 담게 했더니 (약간 그리디 + DP)로 푼문제 그리디에서 문제가 있었다
# 내 알고리즘의 경우
# 1 2 3 4
# 7
# 8
# 이렇게 담았을텐데
# 1 2 7
# 4 6
# 3 5
# 이렇게 담으면 7개로 1개 더 담을수 있다