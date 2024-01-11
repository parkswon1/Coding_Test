import sys
from math import comb

N, M, K = map(int, sys.stdin.readline().split())

def find_kth_string(N, M, K):
    total_length = N + M

    if K > comb(total_length, N):
        return -1

    result = []

    while N > 0 and M > 0:
        combinations_with_a = comb(N + M - 1, N - 1)

        if K <= combinations_with_a:
            result.append('a')
            N -= 1
        else:
            result.append('z')
            M -= 1
            K -= combinations_with_a

    result.extend(['a'] * N)
    result.extend(['z'] * M)

    return ''.join(result)

result = find_kth_string(N, M, K)
print(result)