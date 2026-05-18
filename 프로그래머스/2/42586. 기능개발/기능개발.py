def solution(progresses, speeds):
    answer = []
    index = 0
    n = len(speeds)
    for day in range(1,101):
        count = 0
        while(1):
            if index == n:
                break
            if progresses[index] + (speeds[index] * day) >= 100:
                count += 1
                index += 1
            else:
                break
        if count != 0:
            answer.append(count)
    
        
    return answer