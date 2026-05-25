def solution(n, words):
    answer = [0,0]
    visited = set()
    visited.add(words[0])
    for i in range(1,len(words)):
        if words[i] in visited or words[i - 1][-1] != words[i][0]:
            answer[0] = i % n + 1
            answer[1] = i // n + 1
            return answer
        visited.add(words[i])

    return answer