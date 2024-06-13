

board = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40,
         0, 13, 16, 19, 25, 30, 35,
         22, 24,
         28, 27, 26,
         32, 34, 36, 38, 40, 0]

nextNode = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 21,
            23, 24, 25, 26, 27, 20,
            29, 30,
            31, 32, 20,
            34, 35, 36, 37, 20, 21]

blue = {5: 22, 10: 28, 15: 31}
pieces = [0, 0, 0, 0]

def dfs(turn, score):
    global answer

    if turn == 10:
        answer = max(answer, score)
        return

    dice = dices[turn]
    for i in range(4):
        if pieces[i] == 21:
            continue

        piece = pieces[i]
        nextPiece = piece


        if piece in blue:
            nextPiece = blue[piece]
            dice -= 1

        for _ in range(dice):
            nextPiece = nextNode[nextPiece]
            if nextPiece == 21:
                break

        if nextPiece != 21 and nextPiece in pieces:
            continue

        pieces[i] = nextPiece
        dfs(turn + 1, score + board[nextPiece])
        pieces[i] = piece

dices = list(map(int, input().split()))
answer = 0
dfs(0, 0)
print(answer)