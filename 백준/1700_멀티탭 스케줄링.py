import sys

N, K = map(int,sys.stdin.readline().split())
product = list(map(int,sys.stdin.readline().split()))

plug = []
pcount = [0]*101
for p in product:
    pcount[p] += 1

output = 0
for p in product:
    pcount[p] -= 1
    if len(plug) != N and p not in plug:
        plug.append(p)
    else:
        lowIndex = -1
        lowCount = float('inf')
        for n in range(N):
            if plug[n] == p:
                lowIndex = -1
                break
            elif pcount[plug[n]] < lowCount:
                lowCount = pcount[plug[n]]
                lowIndex = n
        if lowIndex != -1:
            plug[lowIndex] = p
            output += 1

print(output)