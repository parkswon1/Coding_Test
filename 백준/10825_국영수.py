N = int(input())

arr = []
for _ in range(N):
    name, *scores = input().split()
    arr.append((name, *map(int, scores)))

arr.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))

for st in arr:
    print(st[0])