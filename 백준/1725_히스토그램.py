import sys

N = int(sys.stdin.readline())
stack = []
output = -1
for n in range(1, N + 1):
    now = int(sys.stdin.readline())
    start = n
    while (stack):
        if stack[-1][0] > now:
            output = max(output, stack[-1][0] * (n - stack[-1][1]))
            start = stack[-1][1]
            stack.pop()
        else:
            break
    stack.append([now, start])
for i in range(len(stack)):
    output = max(output, stack[i][0] * (N + 1 - stack[i][1]))

print(output)