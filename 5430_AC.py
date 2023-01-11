T = int(input())
for i in range(T):
    command = input()
    n = int(input())
    array = input()
    direction = 1
    frontindex = 1
    backindex =len(array)-2
    errorcode = 0
    for j in command:
        if j == 'R':
            if direction == 1:
                direction = -1
            else:
                direction = 1
        elif j == 'D':
            if direction == 1:
                if frontindex < backindex:
                    while(1):
                        frontindex += 1
                        if array[frontindex] == ',' or frontindex == backindex:
                            frontindex += 1
                            break
                else:
                    print('error')
                    errorcode = 1
                    break
            else:
                if backindex > frontindex:
                    while(1):
                        backindex -= 1
                        if array[backindex] == ',' or frontindex == backindex:
                            backindex -= 1
                            break
                else:
                    print('error')
                    errorcode = 1
                    break
        else:
            print('error')
            errorcode = 1
            break
    if errorcode == 0:
        if direction == 1:
            print('[' + "".join(array[frontindex:backindex+1]) + ']')
        else:
            print('[' + "".join(array[backindex:frontindex-1:-1]) + ']')