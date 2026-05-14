def solution(N, stages):
    answer = []
    count = [0]* (N + 2)
    for s in stages:
        count[s] += 1
    
    total = sum(count)
    cal = []
    for i in range(1, N + 1):
        if total > 0:
            cal.append((i, count[i] / total))
            total -= count[i]
        else:
            cal.append((i, 0))
    
    cal.sort(key=lambda x : (-x[1], x[0]))
    return [s[0] for s in cal]