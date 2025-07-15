from itertools import combinations

def solution(n, q, ans):
    answer = 0
    
    for comb in combinations(range(1, n+1), 5):
        valid = True
        for i in range(len(q)):
            if len(set(q[i]) & set(comb)) != ans[i]:
                valid = False
                break
        
        if valid:
            answer += 1
    
    return answer