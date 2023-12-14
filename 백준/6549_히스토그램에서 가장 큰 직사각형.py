import sys

while(1):
    numbers = list(map(int,sys.stdin.readline().split()))
    N = numbers[0]
    if numbers[0] == 0:
        break
    stack = []
    output = -1
    for n in range(1,N+1):
        now = numbers[n]
        while(stack):
            if stack[-1][0] > now:
                output = max(output, stack[-1][0] * (n-stack[-1][1]))
                stack.pop()
            else:
                break
        stack.append([now,n])
        print(stack,output)
    for i in range(len(stack)):
        output = max(output, stack[i][0] * (N+1-stack[i][1]))

    print(output)