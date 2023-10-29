T = int(input())
for i in range(T):
    command = input()
    n = int(input())
    array= input().rstrip()[1:-1].split(',')
    direction = 1
    frontindex = 0
    backindex = len(array)
    errorcode = 0
    for c in command:
        if c == 'R':
            if direction == 1:
                direction = -1
            else:
                direction =1
        if c == 'D':
            if n == 0:
                errorcode = 1
            if direction == 1:
                if frontindex <backindex:    
                    frontindex +=1
                else:
                    errorcode = 1
            else:
                if backindex > frontindex:
                    backindex -= 1
                else:
                    errorcode = 1
    if errorcode == 1:
        print('error')
    elif n == 0:
        print('[]')
    elif direction == 1:
        print('['+",".join(array[frontindex:backindex])+']')
    elif n == 1:
        print('['+"".join(array[0])+']')
    else:
        print('['+",".join(array[backindex-1:frontindex:-1])+','+array[frontindex]+']')