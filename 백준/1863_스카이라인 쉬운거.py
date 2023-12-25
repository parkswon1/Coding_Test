import sys

N = int(sys.stdin.readline())
stack = []
output = 0
for n in range(N):
    x, y = map(int,sys.stdin.readline().split())
    while(stack):
        if stack[-1] > y:
            stack.pop()
            output += 1
        else:
            break
    if len(stack) == 0 or stack[-1] != y:
        stack.append(y)

while(stack):
    if stack[-1] > 0:
        stack.pop()
        output += 1
    else:
        break
print(output)