def solution(prices):
    answer = [float('inf')] * len(prices)
    stack = []
    for i in range(len(prices)):
        while(stack):
            if stack[-1][0] > prices[i]:
                answer[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            else:
                break
        stack.append([prices[i],i])
        
    while(stack):
        price, i = stack.pop()
        answer[i] = len(prices) - i - 1
    
    return answer