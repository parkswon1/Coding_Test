def solution(topping):
    answer = 0
    frontSet = set()
    backSet = set()
    backDict = {}
    
    for t in topping:
        backSet.add(t)
        if t in backDict:
            backDict[t] += 1
        else:
            backDict[t] = 1
    
    for t in topping:
        frontSet.add(t)
        if t in backDict:
            backDict[t] -= 1
            if backDict[t] <= 0:
                backSet.remove(t)
        
        if len(frontSet) == len(backSet):
            answer += 1
    
    return answer