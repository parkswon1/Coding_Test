import sys

N = int(input())

sticks = []
for n in range(N):
    sticks.append(int(sys.stdin.readline()))

count = 0
top = 0
for i in range(-1,-N-1,-1):
    if sticks[i] > top:
        count += 1
        top = sticks[i]

print(count)