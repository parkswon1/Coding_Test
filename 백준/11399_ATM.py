import sys
N = int(sys.stdin.readline())
P = list(map(int,sys.stdin.readline().split()))

P.sort()
time = 0
totaltime = 0
for i in P:
    time += i
    totaltime += time
print(totaltime)