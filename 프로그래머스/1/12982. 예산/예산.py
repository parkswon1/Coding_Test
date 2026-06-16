def solution(d, budget):
    answer = 0
    d.sort()
    for b in d:
        budget -= b
        if budget < 0:
            return answer
        answer += 1
    return answer