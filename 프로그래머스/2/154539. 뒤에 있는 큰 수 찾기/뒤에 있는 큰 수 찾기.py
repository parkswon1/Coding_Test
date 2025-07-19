from collections import deque

def solution(numbers):
    answer = deque()
    stack = []
    
    for i in range(-1, -len(numbers) - 1, -1):

        while(stack):
            if stack[-1] <= numbers[i]:
                stack.pop()
            else:
                break
        
        if len(stack) == 0:
            answer.appendleft(-1)
        else:
            answer.appendleft(stack[-1])
        
        stack.append(numbers[i])
            
    return list(answer)