# 파일 경로 지정
file_path = "../input.txt"  # 상위 폴더에 있는 경우 상황에 맞게 경로를 조절해주세요.

# 파일 읽어오기 (인코딩을 명시적으로 지정)
with open(file_path, 'r', encoding='utf-8') as file:
    input_data = file.read()

# 문자열을 줄 단위로 나누어 리스트로 변환
input_lines = input_data.strip().split('\n')

import sys
from collections import deque

N, M = map(int, input().split())

people = list(map(int, sys.stdin.readline().split()))
people.sort()
people = deque(people)

answer = 0
while(len(people) > 1):
    back = people.pop()
    front = people.popleft()

    if back + front >= M:
        answer += 1

print(answer)