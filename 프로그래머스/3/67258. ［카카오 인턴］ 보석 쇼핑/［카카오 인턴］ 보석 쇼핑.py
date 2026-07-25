def solution(gems):
    answer = [0,0,float('inf')]
    gCount = len(set(gems))
    print(gCount)
    dict = {}
    front = 0
    for i in range(len(gems)):
        if gems[i] in dict:
            dict[gems[i]] += 1
        else:
            dict[gems[i]] = 1
        
        while len(dict) == gCount:
            if i - front < answer[2]:
                answer = [front, i, i - front]
                
            dict[gems[front]] -= 1
            if dict[gems[front]] == 0:
                dict.pop(gems[front])
            front += 1
        
    return [answer[0] + 1, answer[1] + 1]