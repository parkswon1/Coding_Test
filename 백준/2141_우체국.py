import sys

town = []
peopleCount = 0
N = int(sys.stdin.readline())
for n in range(N):
    a,b = map(int,sys.stdin.readline().split())
    peopleCount += b
    town.append([a,b])

town.sort()
half = peopleCount/2
count = 0
for n in range(N):
    count += town[n][1]
    if count >= half:
        print(town[n][0])
        break