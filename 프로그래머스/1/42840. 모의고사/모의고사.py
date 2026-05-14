def solution(answers):
    answer = []
    fir = [1, 2, 3, 4, 5]
    sec = [2, 1, 2, 3, 2, 4, 2, 5]
    thr = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    firAnswer = 0
    secAnswer = 0
    thrAnswer = 0
    for i in range(len(answers)):
        if fir[i % len(fir)] == answers[i]:
            firAnswer += 1
        if sec[i % len(sec)] == answers[i]:
            secAnswer += 1
        if thr[i % len(thr)] == answers[i]:
            thrAnswer += 1

    maxAnswer = max(firAnswer, secAnswer, thrAnswer)
    if firAnswer == maxAnswer:
        answer.append(1)
    if secAnswer == maxAnswer:
        answer.append(2)
    if thrAnswer == maxAnswer:
        answer.append(3)
    
    return answer