import sys
string = list(sys.stdin.readline().rstrip())
bomb = list(sys.stdin.readline().rstrip())
N = len(bomb)
stack = []
for s in string:
    stack.append(s)
    if stack[-N:] == bomb:
        for _ in range(N):
            stack.pop()

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))