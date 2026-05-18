def solution(n, k, cmd):
    dict = {}
    dict[-1] = [-1, -1]
    dict[0] = [-1, 1]
    for i in range(1, n - 1):
        dict[i] = [i - 1, i + 1]
    dict[n - 1] = [n - 2, -1]
    delStack = []
    
    for c in cmd:
        command = c.split(" ")
        if command[0] == 'U':
            for x in range(int(command[1])):
                k = dict[k][0]
        elif command[0] == 'D':
            for x in range(int(command[1])):
                k = dict[k][1]
        elif command[0] == 'C':
            prev = dict[k][0]
            next = dict[k][1]
            
            dict[prev][1] = next
            dict[next][0] = prev
            
            delStack.append(k)
            
            if next != -1:
                k = next
            else:
                k = prev
                
        elif command[0] == 'Z':
            index = delStack.pop()
            prev = dict[index][0]
            next = dict[index][1]
            
            dict[prev][1] = index
            dict[next][0] = index

    answer = ['O'] * n
    for index in delStack:
        answer[index] = 'X'
        
    return "".join(answer)