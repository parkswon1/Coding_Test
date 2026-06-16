from collections import deque

def solution(people, limit):
    answer = 0

    people.sort()
    pque = deque(people)

    while pque:
        heavy = pque.pop()

        if pque and pque[0] + heavy <= limit:
            pque.popleft()

        answer += 1

    return answer