import sys
K  = int(sys.stdin.readlien())

stack = []
for k in range(K):
    x = int(sys.stdin.readline())
    if x == 0:
        stack.pop(-1)
    else:
        stack.append(x)

print(sum(stack))