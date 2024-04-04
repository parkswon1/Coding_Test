from collections import deque

def solution(n, left, right):
    answer = []
    board = [[1 for i in range(n)] for j in range(n)]
    node = deque([[0,0,1]])
    move = [[1,0],[0,1],[1,1]]
    while(node):
        y, x, z = node.popleft()
        for mv in move:
            my = y + mv[0];
            mx = x + mv[1];
            mz = z + 1;
            if 0 <= my < n and 0 <= mx < n and board[my][mx] == 1:
                board[my][mx] = mz
                node.append([my, mx, mz])
    for l in board:
        answer += l
    return answer[left:right+1]

n = 3
left = 2
right = 5
print(solution(n, left, right))