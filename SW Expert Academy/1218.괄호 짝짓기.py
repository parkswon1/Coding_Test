for test_case in range(1,11):
    N = int(input())
    line = input()
    stack = [line[0]]
    for l in range(1,N):
        if len(stack) != 0:
            left = stack[-1]
            right = line[l]
            if left == '{' and right == '}':
                stack.pop(-1)
            elif left == '(' and right == ')':
                stack.pop(-1)
            elif left == '<' and right == '>':
                stack.pop(-1)
            elif left == '[' and right == ']':
                stack.pop(-1)
            else:
                stack.append(right)
        else:
            stack.append(line[l])

    if len(stack) != 0:
        check = 0
    else:
        check = 1

    print(f'#{test_case}', check)