T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        A, B = B, A
        N, M = M, N

    answer = 0

    for start in range(M - N + 1):
        total = 0

        for i in range(N):
            total += A[i] * B[start + i]

        answer = max(answer, total)

    print(f"#{t} {answer}")