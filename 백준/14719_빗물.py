import sys

H, W = map(int,sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split()))

stack = [numbers[0]]
output = 0

for n in range(1,W):
    if stack[-1] > numbers[n]:
        stack.append(numbers[n])
    else:
        if stack[0] < numbers[n]:
            low = stack[0]
            while(stack):
                output += low - stack.pop()
        else: #n보다 stack[0]가 크거나 같을떄
            for i in range(len(stack)-1,0,-1):
                if stack[i] < numbers[n]:
                    output += numbers[n] - stack[i]
                    stack[i] = numbers[n]
                else:
                    break
        stack.append(numbers[n])

print(output)