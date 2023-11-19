T = int(input())
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if N < M:
        A, B = B, A
        N, M = M, N

    output = 0
    for n in range(N-M+1):
        total = 0
        for m in range(M):
            total += A[n + m] * B[m]
        output = max(output, total)
    print(f'#{test_case}',output)