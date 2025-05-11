import sys
input = sys.stdin.readline

N, K = map(int, input().split())
X = []

for _ in range(N):
    A, B = map(int, input().split())
    X.append(B - A)

X.sort()

if X[K - 1] < 0:
    print(0)
else:
    print(X[K - 1])