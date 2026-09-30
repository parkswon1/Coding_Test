def solution(number, k):
    answer = ''
    stack = []
    for n in number:
        n = int(n)
        while stack:
            if stack[-1] < n and k > 0:
                k -= 1
                stack.pop()
            else:
                break
        stack.append(n)
    for i in range(k):
        stack.pop()
    
    return ''.join(map(str,stack))