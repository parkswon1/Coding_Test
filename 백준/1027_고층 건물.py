import sys

N = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))

output = 0
count = [0] * N
for n in range(N):
    for m in range(n+1,N):
        cant = 0
        for i in range(n+1,m):
            y = ((b[m] - b[n])/(m - n)) * (i - n) + b[n]
            if b[i] >= y:
                cant = 1
                break

        if cant == 0:
            count[n] += 1
            count[m] += 1

print(max(count))