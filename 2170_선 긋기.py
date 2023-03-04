import sys
N = int(sys.stdin.readline())

lines = []

for i in range(N):
    lines.append(list(map(int,sys.stdin.readline().split())))

lines.sort()

front = lines[0][0]
back = lines[0][1]

output = 0

for i in range(1,N):
    if lines[i][0] <= back:
        back = max(lines[i][1],back)
    else:
        output += abs(back - front)
        front = lines[i][0]
        back = lines[i][1]

print(output + abs(back - front))