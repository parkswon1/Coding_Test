def solution(board, moves):
    answer = 0
    stack = []
    for mv in moves:
        mv = mv - 1
        for i in range(len(board)):
            if board[i][mv] != 0:
                if len(stack) != 0 and stack[-1] == board[i][mv]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[i][mv])
                board[i][mv] = 0
                break

    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))