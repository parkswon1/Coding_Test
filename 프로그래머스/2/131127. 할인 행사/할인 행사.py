def solution(want, number, discount):
    answer = 0
    wantDict = {}
    for i in range(len(number)):
        wantDict[want[i]] = number[i]

    discCountDict = {}

    for i in range(min(10, len(discount))):
        discCountDict[discount[i]] = discCountDict.get(discount[i], 0) + 1

    def checkAnswer():
        for i in range(len(want)):
            if wantDict[want[i]] != discCountDict.get(want[i], 0):
                return False
        return True

    if len(discount) >= 10 and checkAnswer():
        answer += 1

    for i in range(10, len(discount)):
        if len(discount) < 10:
            break
        front = i - 10
        discCountDict[discount[front]] = discCountDict.get(discount[front], 0) - 1
        if discCountDict[discount[front]] == 0:
            del discCountDict[discount[front]]

        discCountDict[discount[i]] = discCountDict.get(discount[i], 0) + 1

        if checkAnswer():
            answer += 1

    return answer
