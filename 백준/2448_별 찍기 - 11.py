def tree(deep,node):
    next_node = []
    for n in node:
        new = maketree(deep,n)
        if len(next_node) != 0 and next_node[-1] == new[0]:
            next_node.pop()
        else:
            next_node.append(new[0])
        next_node.append(new[1])
    if deep + 3 != N:
        tree(deep + 3, next_node)

def maketree(deep,n):
    board[deep][n] = '*'
    board[deep+1][n-1] = '*'
    board[deep+1][n+1] = '*'
    for i in range(5):
        board[deep+2][n-2+i] = '*'
    return [n-3,n+3]


import sys
sys.setrecursionlimit(10**7)
N = int(input())
board = []
for _ in range(N):
    board.append([' ']*N*2)
tree(0,[N-1])

for i in range(N):
    print(''.join(board[i]))