from collections import deque

def solution(queue1, queue2):
    answer = 0
    que1Value = sum(queue1)
    que2Value = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    while(1):
        if que1Value > que2Value:
            temp = queue1.popleft()
            que1Value -= temp
            que2Value += temp
            queue2.append(temp)
        elif que2Value > que1Value:
            temp = queue2.popleft()
            que2Value -= temp
            que1Value += temp
            queue1.append(temp)
        else:
            return answer
        answer += 1
        if answer > 600000:
            return -1

queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]
print(solution(queue1, queue2))