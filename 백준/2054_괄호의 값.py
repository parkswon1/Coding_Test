import sys

right = list(sys.stdin.readline().rstrip())
left = []
stack = []
output = 0
check = 0
err = 0
for r in right:
    if r == '(':
        stack.append(2)
        left.append('(')
        check = 1
    elif r == '[':
        stack.append(3)
        left.append('[')
        check = 1
    elif len(left) != 0:
        if (r == ')' and left[-1] == '(') or (r == ']' and left[-1] == '['):
            if check == 1:
                put = 1
                for i in range(len(stack)):
                    put *= stack[i]
                output += put
                check = 0
            stack.pop()
            left.pop()
        else:
            err = 1
            break
    else:
        err = 1
        break

if len(left) == 0 and err == 0:
    print(output)
else:
    print(0)