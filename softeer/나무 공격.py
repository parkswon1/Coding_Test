import sys

N, M = list(map(int, sys.stdin.readline().split()))

personCount = []
for n in range(N):
    line = sys.stdin.readline().split()
    personCount.append(line.count('1'))

for _ in range(2):
    start, end = list(map(int, sys.stdin.readline().split()))
    for i in range(start-1, end):
        personCount[i] -= 1
        if personCount[i] < 0:
            personCount[i] = 0

print(sum(personCount))