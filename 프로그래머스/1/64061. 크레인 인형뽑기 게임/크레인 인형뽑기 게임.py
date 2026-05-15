def solution(board, moves):
    stacks = []
    for x in range(len(board[0])):
        stack = []
        for y in range(len(board) -1, -1, -1):
            if board[y][x] == 0:
                continue
            stack.append(board[y][x])
        stacks.append(stack)
    # print(stacks)
    
    answer = 0
    temp = []
    for m in moves:
        if stacks[m - 1]:
            a = stacks[m - 1].pop()
            temp.append(a)
        
        if len(temp) > 1 and temp[-1] == temp[-2]:
            temp.pop()
            temp.pop()
            answer += 2
                
    return answer