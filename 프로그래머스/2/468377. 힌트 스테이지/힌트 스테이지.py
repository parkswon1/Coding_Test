import itertools

def solution(cost, hints):
    answer = float('inf')
    combs = list(itertools.product((0,1), repeat=len(hints)))
    
    #comb는 각 스테이지에 힌트를 구매하는가 1이면 구매 아니면 구매하지 않음
    #hints의 각각 hint의 0 인덱스는 힌트의 가격 나머지는 힌트 할인권
    #따라서 hint를 구매시 comb에 해당하는 hint 인덱스가 1일경우 hint[0]를 총가격에 부여
    #그리고 힌트권 번호를 담는 index 배열에 해당 힌트 index에 +1을 함
    for comb in combs:
        hintIndex = [0] * (len(cost)+1)
        temp = 0
        for i in range(len(comb)):
            if comb[i] == 1:
                temp += hints[i][0]
                for j in range(1, len(hints[i])):
                    hintIndex[hints[i][j]] += 1
        
        for h in range(len(cost)):
            temp += cost[h][min(hintIndex[h+1], len(cost) - 1)]
        
        answer = min(answer, temp)
        
    return answer