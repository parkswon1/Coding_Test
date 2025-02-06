import sys

# 입력 받기
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 누적 합 배열 초기화 (패딩 포함)
dp = [[0] * (M + 1) for _ in range(N + 1)]

# 누적 합 계산
for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = board[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

# 부분합 최대값 찾기
output = -float('inf')
for i1 in range(1, N + 1):
    for j1 in range(1, M + 1):
        for i2 in range(i1, N + 1):
            for j2 in range(j1, M + 1):
                # (i1, j1) ~ (i2, j2) 부분합
                total = dp[i2][j2] - dp[i1-1][j2] - dp[i2][j1-1] + dp[i1-1][j1-1]
                output = max(output, total)

print(output)