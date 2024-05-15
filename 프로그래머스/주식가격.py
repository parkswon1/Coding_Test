def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i in range(len(prices)):
        p = prices[i]
        while(stack):
            if stack[-1][0] > p:
                poped = stack.pop()
                answer[poped[1]] = i - poped[1]
            else:
                break
        stack.append([p,i])

    for s in stack:
        answer[s[1]] = i - s[1]

    return answer

price = [1,2,3,2,3]
print(solution(price))