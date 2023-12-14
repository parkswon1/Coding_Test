import sys

N= int(sys.stdin.readline())

bilding = []

for _ in range(N):
    bilding.append(int(sys.stdin.readline()))

right = []
output = 0
while(bilding):
    now = bilding.pop()
    count = 0
    while(right):
        if right[-1][0] < now:
            count += right[-1][1] + 1
            right.pop()
        else:
            break
    right.append([now,count])
    output += count

print(output)