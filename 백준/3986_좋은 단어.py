import sys

N = int(sys.stdin.readline())

output = 0
for n in range(N):
    right = list(sys.stdin.readline().rstrip())
    left = []
    for r in right:
        if len(left) == 0:
            left.append(r)
        else:
            if left[-1] == r:
                left.pop()
            else:
                left.append(r)
    if len(left) == 0:
        output += 1

print(output)