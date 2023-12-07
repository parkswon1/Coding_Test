import sys

c = []
for _ in range(6):
    c.append([0,0])
N, K = map(int,sys.stdin.readline().split())

for n in range(N):
    x,y = map(int,sys.stdin.readline().split())
    c[y-1][x] += 1

count = 0
for y in range(6):
    for x in range(2):
        num = c[y][x]
        count += num//K
        if num%K != 0:
            count += 1

print(count)
