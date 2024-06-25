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