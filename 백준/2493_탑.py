import sys

N = int(sys.stdin.readline())
towers = list(map(int,sys.stdin.readline().split()))
stack = [[towers[0],0]]
output = [0]
for n in range(1,N):
    while(stack):
        if stack[-1][0] <= towers[n]:
            stack.pop()
        else:
            output.append(stack[-1][1]+1)
            stack.append([towers[n],n])
            break
    if len(stack) == 0:
        stack.append([towers[n], n])
        output.append(0)
print(*output)