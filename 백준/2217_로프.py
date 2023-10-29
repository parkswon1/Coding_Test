import sys
N = int(sys.stdin.readline())

rope = []
for i in range(N):
    rope.append(int(sys.stdin.readline()))

rope.sort()

Mweight = 0
for i in range(-1,-(N+1),-1):
    if rope[i]*(-i) > Mweight:
        Mweight = rope[i]*(-i)

print(Mweight)