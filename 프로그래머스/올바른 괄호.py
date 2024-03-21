def solution(s):
    answer = True
    stack = []
    for par in s:
        if len(stack) == 0:
            stack.append(par)
        else:
            if par == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(par)

    return len(stack) == 0

print(solution("(()("))