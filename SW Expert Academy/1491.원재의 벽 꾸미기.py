T = int(input())

for t in range(1, T+1):
    N, A, B = map(int, input().split())

    min_value = A * N

    for R in range(1, N+1):
        for C in range(1, N//R+1):
            value = A * abs(R - C) + B * (N - R * C)
            min_value = min(min_value, value)

    print(f"#{t} {min_value}")