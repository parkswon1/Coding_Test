from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    infoDict = defaultdict(list)

    for item in info:
        itemList = item.split(" ")
        score = int(itemList[4])
        masks = getPossibleMasks(itemList)
        for maskKey in masks:
            infoDict[maskKey].append(score)

    for key in infoDict:
        infoDict[key].sort()

    for queryStr in query:
        queryList = queryStr.replace(" and ", " ").split(" ")
        queryBit = parseQueryToBit(queryList)
        targetScore = int(queryList[4])

        scores = infoDict[queryBit]
        if scores:
            idx = bisect_left(scores, targetScore)
            answer.append(len(scores) - idx)
        else:
            answer.append(0)

    return answer


def cal(itemList):
    temp = 0
    if itemList[0] == 'cpp': temp |= (1 << 0)
    elif itemList[0] == 'java': temp |= (1 << 1)
    elif itemList[0] == 'python': temp |= (1 << 2)

    if itemList[1] == 'backend': temp |= (1 << 3)
    elif itemList[1] == 'frontend': temp |= (1 << 4)

    if itemList[2] == 'junior': temp |= (1 << 5)
    elif itemList[2] == 'senior': temp |= (1 << 6)

    if itemList[3] == 'chicken': temp |= (1 << 7)
    elif itemList[3] == 'pizza': temp |= (1 << 8)

    return temp


def parseQueryToBit(queryList):
    queryBit = 0
    if queryList[0] == 'cpp': queryBit |= (1 << 0)
    elif queryList[0] == 'java': queryBit |= (1 << 1)
    elif queryList[0] == 'python': queryBit |= (1 << 2)

    if queryList[1] == 'backend': queryBit |= (1 << 3)
    elif queryList[1] == 'frontend': queryBit |= (1 << 4)

    if queryList[2] == 'junior': queryBit |= (1 << 5)
    elif queryList[2] == 'senior': queryBit |= (1 << 6)

    if queryList[3] == 'chicken': queryBit |= (1 << 7)
    elif queryList[3] == 'pizza': queryBit |= (1 << 8)

    return queryBit


def getPossibleMasks(itemList):
    langBit = cal([itemList[0], '', '', ''])
    groupBit = cal(['', itemList[1], '', ''])
    careerBit = cal(['', '', itemList[2], ''])
    foodBit = cal(['', '', '', itemList[3]])

    bits = [langBit, groupBit, careerBit, foodBit]
    masks = []

    for i in range(16):
        currentMask = 0
        for j in range(4):
            if (i >> j) & 1:
                currentMask |= bits[j]
        masks.append(currentMask)

    return masks