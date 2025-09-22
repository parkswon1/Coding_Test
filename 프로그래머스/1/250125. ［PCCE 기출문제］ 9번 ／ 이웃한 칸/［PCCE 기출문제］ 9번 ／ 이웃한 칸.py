def solution(board, h, w):
    answer = 0
    move = ((1,0),(-1,0),(0,1),(0,-1))
    
    for mv in move:
        mh = h + mv[0]
        mw = w + mv[1]
        if 0 <= mh < len(board) and 0 <= mw < len(board[0]):
            if board[h][w] == board[mh][mw]:
                answer += 1
    
    return answer