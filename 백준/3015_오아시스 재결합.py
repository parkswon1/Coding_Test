import sys

N = int(sys.stdin.readline())
stack = []
output = 0
for _ in range(N):
    now = int(sys.stdin.readline())
    count = 1
    while(stack):
        if stack[-1][0] < now:
            output += stack[-1][1]
            stack.pop()
        elif stack[-1][0] == now:
            output += stack[-1][1]
            count += stack[-1][1]
            stack.pop()
        else:
            output += 1
            break
    stack.append([now,count])

print(output)