import sys

N = int(sys.stdin.readline())
bildings = list(map(int, sys.stdin.readline().split()))
near = [float('inf')] * N
count = [0] * N

stack = [[bildings[0],0]]
for n in range(1,N):
    while stack:
            if stack[-1][0] < bildings[n]:
                stack.pop()
            elif stack[-1][0] == bildings[n]:
                stack.pop()
            else:
                break

    count[n] += len(stack)
    if len(stack) != 0:
        if abs(stack[-1][1] - n) < abs(near[n]):
            near[n] = stack[-1][1] - n

    stack.append([bildings[n],n])

stack = [[bildings[N - 1], N - 1]]
for n in range(N - 2, -1, -1):
    while stack:
        if stack[-1][0] < bildings[n]:
            stack.pop()
        elif stack[-1][0] == bildings[n]:
            stack.pop()
        else:
            break

    count[n] += len(stack)
    if len(stack) != 0:
        if abs(stack[-1][1] - n) < abs(near[n]):
            near[n] = stack[-1][1] - n

    stack.append([bildings[n], n])

for i in range(N):
    if count[i] != 0:
        print(count[i], i + near[i] + 1)
    else:
        print(0)