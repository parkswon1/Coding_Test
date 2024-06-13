# 파일 경로 지정
file_path = "../input.txt"  # 상위 폴더에 있는 경우 상황에 맞게 경로를 조절해주세요.

# 파일 읽어오기 (인코딩을 명시적으로 지정)
with open(file_path, 'r', encoding='utf-8') as file:
    input_data = file.read()

# 문자열을 줄 단위로 나누어 리스트로 변환
input_lines = input_data.strip().split('\n')

import sys, copy

diceNums = list(map(int, input_lines[0].split()))

board = [[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40],
         [0,13,16,19,25,30,35,40],
         [0,22,24,25,30,35,40],
         [0,28,27,26,25,30,35,40]]

blue = {10: 1, 20: 2, 30: 3}

answer = -1

def dfs(turnindex, pieceList, score):
    global answer
    if turnindex == 10:
        answer = max(answer, score)
        return

    dice = diceNums[turnindex]
    for i in range(4):
        y, x = pieceList[i]
        if y != -1:  # 말이 도착 칸에 있지 않으면
            my, mx = y, x
            if board[y][x] in blue:  # 파란색 칸인 경우 경로 변경
                my = blue[board[y][x]]
                mx = 0

            mx += dice  # 주사위 수만큼 이동

            if mx >= len(board[my]):  # 도착 칸을 넘어서는 경우
                pieceList[i] = [-1, -1]
                dfs(turnindex + 1, pieceList, score)
                pieceList[i] = [y, x]
            else:
                next_position = [my, mx]
                if next_position not in pieceList:  # 이동할 칸에 다른 말이 없는 경우
                    pieceList_copy = copy.deepcopy(pieceList)
                    pieceList_copy[i] = next_position
                    dfs(turnindex + 1, pieceList_copy, score + board[my][mx])

dfs(0,[[0,0],[0,0],[0,0],[0,0]],0)
print(answer)