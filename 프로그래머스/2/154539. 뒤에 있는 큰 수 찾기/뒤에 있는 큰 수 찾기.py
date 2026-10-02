def solution(numbers):
    N = len(numbers)
    answer = [-1] * N
    stack = []
    for i in range(N):
        now = numbers[i]
        while stack:
            if stack[-1][0] >= now:
                break
            
            num, index = stack.pop()
            answer[index] = now
        
        stack.append((now, i))

    return answer