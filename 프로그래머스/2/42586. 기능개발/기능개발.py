from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    day = 0
    for i in range(len(progresses)):
        p = progresses[i]
        s = speeds[i]
        if day * s + p >= 100:
            answer[-1] += 1
        else:
            day += math.ceil((100 - (day * s + p)) / s)
            answer.append(1)
            
    return answer