import sys
from collections import deque
N, K = map(int,sys.stdin.readline().split())
numbers = deque(list(sys.stdin.readline().rstrip()))
stack = [numbers.popleft()]

count = 0
check = 0
while(numbers):
    now = numbers.popleft()
    while(stack):
        if int(stack[-1]) < int(now):
            stack.pop()
            count += 1
            if count == K:
                check = 1
                break
        else:
            break
    stack.append(now)
    if check == 1:
        break
while(numbers):
    stack.append(numbers.popleft())
while count < K:
    count += 1
    stack.pop()
print(''.join(stack))