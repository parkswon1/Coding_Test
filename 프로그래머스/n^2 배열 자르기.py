def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        answer.append(max(i // n, i % n) + 1)
    return answer

n = 4
left = 4
right = 14
print(solution(n, left, right))