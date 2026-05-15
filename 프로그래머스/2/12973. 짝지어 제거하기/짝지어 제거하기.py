def solution(S):

    stack = []
    for s in S:
        stack.append(s)
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    if len(stack) > 0:
        return 0
    return 1