import sys

N, M, L, K = map(int, sys.stdin.readline().split())

stars = []
for k in range(K):
    stars.append(list(map(int, sys.stdin.readline().split())))

answer = 0

for x1, y1 in stars:
    for x2, y2 in stars:
        count = 0
        for x, y in stars:
            if x1 <= x <= x1 + L and y2 <= y <= y2 + L:
                count += 1
        answer = max(answer, count)

print(K - answer)