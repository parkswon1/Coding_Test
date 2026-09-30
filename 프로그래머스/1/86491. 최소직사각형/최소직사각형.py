def solution(sizes):
    answer = 0
    가로 = []
    세로 = []
    for s in sizes:
        가로.append(max(s))
        세로.append(min(s))    
    return max(가로) * max(세로)