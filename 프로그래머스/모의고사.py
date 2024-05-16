def solution(answers):
    answer = []
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    N = len(answers)
    first = first * (N//5 + 1)
    second = second * (N//8 + 1)
    third = third * (N//10 + 1)
    count = [0,0,0]
    maxCount = 0
    for i in range(N):
        if answers[i] == first[i]:
            count[0] += 1
        if answers[i] == second[i]:
            count[1] += 1
        if answers[i] == third[i]:
            count[2] += 1
        maxCount = max(count)

    for i in range(3):
        c = count[i]
        if c == maxCount:
            answer.append(i + 1)
    return answer

answers = [1,3,2,4,2]
print(solution(answers))