N = int(input())
limit = N*N
output= 0
def DFS(board,index,count):
    global output
    if count == N:
        output += 1
    while(1):
        if board[index] == 0:
            break
        elif index == limit-1 :
            break
        else:
            index += 1

    if index != limit-1:  
        print(board)
        DFS(board,index+1,count)
    width = (index//N)*N
    for i in range(width,width+N):
        board[i] = 1
    for i in range(index,limit,N):
        board[i] = 1
    for i in range(index,limit,N+1):
        board[i] = 1
    if index != limit-1:   
        DFS(board,index+1,count+1)



node = 0
board = [0]*N*N
count = 0
DFS(board,node+1,count)
board = [0]*limit
width = (node//N)*N
for i in range(width,width+N):
    board[i] = 1
for i in range(node,limit,N):
    board[i] = 1
for i in range(node,limit,N+1):
    board[i] = 1
node += 1
while(1):
    if board[node] == 0:
        break
    elif node == limit-1 :
        break
    else:
        node += 1
DFS(board,node+1,count+1)