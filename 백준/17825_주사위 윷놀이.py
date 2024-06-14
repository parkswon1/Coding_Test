diceNums = list(map(int, input().split()))

board = [0, 2, 4, 6, 8,
         10, 12, 14, 16, 18,
         20, 22, 24, 26, 28,
         30, 32, 34, 36, 38,
         40, 13, 16, 19, 25,
         22, 24, 28, 27, 26,
         30, 35, 0]

move = [[1], [2], [3], [4], [5],
         [6, 21], [7], [8], [9], [10],
         [11, 25], [12], [13], [14], [15],
         [16, 27], [17], [18], [19], [20],
         [32], [22], [23], [24], [30],
         [26], [24], [28], [29], [24],
         [31], [20], [32]]

turn = 0
list = [0,0,0,0]
answer = 0
def dfs(turn, list, score):
    global answer

    if turn == 10:
        answer = max(answer , score)
        return

    for i in range(4):
        mx = list[i]

        if len(move[mx]) == 2:
            mx = move[mx][1]
        else:
            mx = move[mx][0]

        for _ in range(1, diceNums[turn]):
            mx = move[mx][0]

        if mx == 32 or (mx < 32 and mx not in list):
            x = list[i]
            list[i] = mx
            dfs(turn+1, list, score + board[mx])
            list[i] = x

dfs(0, list, 0)
print(answer)