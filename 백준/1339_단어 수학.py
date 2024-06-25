file_path = "../input.txt"  # 상위 폴더에 있는 경우 상황에 맞게 경로를 조절해주세요.

# 파일 읽어오기 (인코딩을 명시적으로 지정)
with open(file_path, 'r', encoding='utf-8') as file:
    input_data = file.read()

# 문자열을 줄 단위로 나누어 리스트로 변환
input_lines = input_data.strip().split('\n')

import sys

N = int(sys.stdin.readline())
dict = {}
for n in range(N):
    word = list(sys.stdin.readline().rstrip())
    for i in range(len(word)):
        j = -i - 1
        if word[j] in dict:
            dict[word[j]] += int('1' + '0'*i)
        else:
            dict[word[j]] = int('1' + '0'*i)

wordCountList = []
for d in dict:
    wordCountList.append(dict[d])

wordCountList.sort(reverse=True)
answer = 0
for i in range(len(wordCountList)):
    answer += wordCountList[i] * (9 - i)

print(answer)