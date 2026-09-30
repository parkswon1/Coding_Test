from collections import deque

def solution(priorities, location):
    answer = 0
    s = deque(sorted(priorities, reverse=True))
    p = deque([])
    for i in range(len(priorities)):
        p.append((priorities[i], i))
    while(p):
        pro, i = p.popleft()
        if pro == s[0]:
            s.popleft()
            answer += 1
            if i == location:
                return answer
        else:
            p.append((pro, i))
                
    return answer