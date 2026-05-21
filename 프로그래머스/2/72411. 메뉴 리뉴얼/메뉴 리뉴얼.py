from itertools import combinations
from collections import Counter

def solution(orders, course):
    finalAnswer = []
    
    for courseSize in course:
        combinationList = []
        
        for currentOrder in orders:
            sortedOrder = sorted(currentOrder)
            
            for comboTuple in combinations(sortedOrder, courseSize):
                combinationList.append("".join(comboTuple))
                
        if not combinationList:
            continue
            
        combinationCounter = Counter(combinationList)
        
        maxOrderCount = max(combinationCounter.values())
        
        if maxOrderCount >= 2:
            for menuCombination, orderCount in combinationCounter.items():
                if orderCount == maxOrderCount:
                    finalAnswer.append(menuCombination)
                    
    return sorted(finalAnswer)