def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        p = prices[i]
        while stack:
            if stack[-1][0] > p:
                price, index = stack.pop()
                answer[index] = i - index
            else:
                break
        
        stack.append((p, i))
    
    while stack:
        price, index = stack.pop()
        answer[index] = i - index
                
    return answer