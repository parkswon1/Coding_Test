def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    c = -float('inf')
    for r in routes:
        if r[0] <= c <= r[1]:
            continue
        else:
            c = r[1]
            answer += 1
    return answer