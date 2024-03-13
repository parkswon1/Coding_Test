import sys, copy

def search(board):
    up_board = [[0 for o in range(N)] for _ in range(N)]
    down_board = [[0 for o in range(N)] for _ in range(N)]
    for x in range(N):
        stack = []
        for y in range(N):
            if board[y][x] != 0:
                stack.append(board[y][x])

        while len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack[-1] *= 2
            else:
                break



# 파일 경로 지정
file_path = "../input.txt"  # 상위 폴더에 있는 경우 상황에 맞게 경로를 조절해주세요.

# 파일 읽어오기 (인코딩을 명시적으로 지정)
with open(file_path, 'r', encoding='utf-8') as file:
    input_data = file.read()

# 문자열을 줄 단위로 나누어 리스트로 변환
input_lines = input_data.strip().split('\n')

N = int(input_lines[0])
board = []
for n in range(N):
    board.append(input_lines[n + 1])

search(board)