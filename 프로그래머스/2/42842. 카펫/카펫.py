def solution(brown, yellow):
    answer = []
    if yellow == 1:
        return [3,3]
    for 가로 in range(1, yellow // 2 + 1):
        if yellow % 가로 != 0:
            continue    
        세로 = yellow // 가로
        if 4 + (세로 * 2) + (가로 * 2) == brown:
            return [세로 + 2, 가로 + 2]
    return answer