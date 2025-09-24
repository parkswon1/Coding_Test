def solution(s):
    n = len(s)
    if n == 0:
        return 0

    s2 = s + s  
    openSet = {'(', '[', '{'}
    pairMap = {')': '(', ']': '[', '}': '{'}

    def isValid(segment):
        stack = []
        for ch in segment:
            if ch in openSet:
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairMap.get(ch, ''):
                    return False
                stack.pop()
        return not stack

    answer = 0
    for i in range(n):
        if isValid(s2[i:i + n]):
            answer += 1
    return answer
