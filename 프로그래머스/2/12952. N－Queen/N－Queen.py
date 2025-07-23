board = []
answer = 0
n = 0

def solution(input_n):
    global n, answer
    answer = 0
    n = input_n
    backTracking(0)
    return answer

def isValid(row, col):
    for r in range(row):
        if board[r] == col or abs(board[r] - col) == row - r:
            return False
    return True

def backTracking(row):
    global answer
    if row == n:
        answer += 1
        return
    for col in range(n):
        if isValid(row, col):
            board.append(col)
            backTracking(row + 1)
            board.pop()