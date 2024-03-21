def solution(word):
    global answer, count
    count = 0
    recurcive("",word)
    return answer

def recurcive(words,word):
    global answer, count
    if words == word:
        answer = count
    elif len(words) != 5:
        for a in alpha:
            count += 1
            recurcive(words+a,word)

alpha = ["A","E","I","O","U"]
print(solution("I"))