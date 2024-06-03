T, W = map(int, input().split())

W = W + 1
DP = [[0 for w in range(W)] for t in range(T)]

first = int(input())
for w in range((first + 1)%2, W, 2):
    DP[0][w] = 1

for t in range(1, T):
    jadoPlus = int(input()) - 1

    DP[t][0] = DP[t - 1][0]
    if jadoPlus == 0:
        DP[t][0] += 1

    for w in range(1, W):
        DP[t][w] = max(DP[t - 1][w - 1], DP[t - 1][w])
        if w % 2 == jadoPlus:
            DP[t][w] += 1

print(max(DP[T - 1]))