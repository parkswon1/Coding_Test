#dict를 2개를 두고 값을 담는다.
#dict의 key값이 있는경우 +1 0이 될경우 dict에서 아예 뺴버린다.
#처음에 왼쪽놈한테 dict를 한번 싹 담는다.
#이제 한번더 for문을 돌려서 오른쪽놈한테 dict를 1개씩 양보하면서 양쪽 dict의 길이를 비교하여 count 정답을 센다 같으면 +1

from collections import defaultdict

def solution(topping):
    answer = 0
    leftDict = {}
    rightSet = set()
    
    for t in topping:
        if t in leftDict:
            leftDict[t] += 1
        else:
            leftDict[t] = 1
    
    for t in topping:
        leftDict[t] -= 1
        if leftDict[t] == 0:
            leftDict.pop(t)
        
        rightSet.add(t)
        
        if len(leftDict) == len(rightSet):
            answer += 1
        
    
    return answer