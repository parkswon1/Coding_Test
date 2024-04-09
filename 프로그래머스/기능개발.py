from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    day = 1
    while(progresses):
        count = 0
        while(progresses):
            if progresses[0] + speeds[0] * day >= 100:
                progresses.popleft()
                speeds.popleft()
                count += 1
            else:
                break
        if count != 0:
            answer.append(count)
        day += 1
    return answer

progress = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progress, speeds))