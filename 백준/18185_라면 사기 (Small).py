import sys

N = int(sys.stdin.readline())
pactory = list(map(int,sys.stdin.readline().split())) +[0, 0]
output = 0
for n in range(N):
    if pactory[n + 2] < pactory[n + 1]:
        diff = min(pactory[n], pactory[n + 1] - pactory[n + 2])
        pactory[n] -= diff
        pactory[n + 1] -= diff
        output += diff * 5
        diff = min(pactory[n], pactory[n + 1], pactory[n + 2])
        pactory[n] -= diff
        pactory[n + 1] -= diff
        pactory[n + 2] -= diff
        output += diff * 7
    else:
        diff = min(pactory[n + 2], pactory[n + 1], pactory[n])
        pactory[n + 2] -= diff
        pactory[n + 1] -= diff
        pactory[n] -= diff
        output += diff * 7
        diff = min(pactory[n + 1], pactory[n + 0])
        pactory[n + 1] -= diff
        pactory[n] -= diff
        output += diff * 5
    output += pactory[n] * 3

print(output)