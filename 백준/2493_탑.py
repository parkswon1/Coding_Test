import sys

N = int(sys.stdin.readline())

tower = list(map(int,sys.stdin.readline().split()))

stack = []

output = []
for n in range(N):
    M = len(stack)
    if M == 0:
        output.append(0)
        stack.append(tower)
    for m in range(M):
        if stack[-1] < tower[n]:
            stack.pop()
        else:
            