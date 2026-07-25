def solution(targets):
    answer = 0
    targets.sort(key=lambda x : x[1])
    m = -float('inf')
    for start, end in targets:
        if start < m < end:
            continue
        m = end - 0.5
        answer += 1
        print(m)
        
    return answer