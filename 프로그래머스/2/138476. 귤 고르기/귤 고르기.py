from collections import Counter

def solution(k, tangerine):
    answer = 0
    countDict = Counter(tangerine)
    sortDcit = sorted(countDict.items(), key=lambda x: x[1], reverse=True)
    
    for key, count in sortDcit:
        k -= count
        answer += 1
        if k <= 0:
            return answer
    return answer