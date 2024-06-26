import sys

N, K = map(int, sys.stdin.readline().split())

ab = []
ac = []
bc = []

for i in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    ab.append(a + b)
    ac.append(a + c)
    bc.append(b + c)

ab.sort(reverse=True)
ac.sort(reverse=True)
bc.sort(reverse=True)

maxAb = sum(ab[:K])
maxAc = sum(ac[:K])
maxBc = sum(bc[:K])

print(max(maxAb , maxAc, maxBc))