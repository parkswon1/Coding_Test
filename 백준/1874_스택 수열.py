import sys
n = int(sys.stdin.readline())
number = 0
stack = []
output = []
check = 0
for j in range(n):
    i = int(sys.stdin.readline())
    if number < i:
        while(number < i):
            number +=1
            output.append('+')
            stack.append(number)
        output.append('-')
        stack.pop()
    elif number > i:
        a= stack.pop()
        if a != i:
            check = 1
            print('NO')
            break
        else:
            output.append('-')
if check == 0:
    for k in output:
        print(k)