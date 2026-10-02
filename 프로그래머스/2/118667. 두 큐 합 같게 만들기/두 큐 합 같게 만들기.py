from collections import deque

def solution(queue1, queue2):
    answer = -2
    goal = (sum(queue1) + sum(queue2)) //2
    c1 = sum(queue1)
    q1 = deque(queue1)
    c2 = sum(queue2)
    q2 = deque(queue2)
    count = 0

    while c1 != c2:  #앞으로뺴기
        while c1 > goal and q1:
            count += 1
            temp = q1.popleft()
            c1 -= temp
            c2 += temp
            q1.append(temp)
            
        while c2 > goal and q2:
            count += 1
            temp = q2.popleft()
            c2 -= temp
            c1 += temp
            q1.append(temp)
        
        if len(q1) == 0 or len(q2) == 0:
            return -1
    
    return count