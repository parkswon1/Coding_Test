import sys

N = int(input())
light = list(map(int, sys.stdin.readline().rstrip()))
answer = list(map(int, sys.stdin.readline().rstrip()))

def change(light, target):
    count = 0
    for n in range(1, N):
        if light[n - 1] == target[n - 1]: continue

        count += 1
        for i in range(n - 1, n + 2):
            if i < N: light[i] = 1 - light[i]

    if light == target:
        return count
    else:
        return float('inf')

output = change(light[:], answer)

light[0] = 1 - light[0]
light[1] = 1 - light[1]
output = min(output, change(light[:], answer) + 1)
if output == float('inf'):
    print(-1)
else:
    print(output)