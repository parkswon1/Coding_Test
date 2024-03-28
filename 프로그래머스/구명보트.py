from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while(len(people) > 1):
        back = people.pop()
        if back + people[0] <= limit:
            people.popleft()
        answer += 1

    if len(people) == 1 and people.pop() <= limit:
        answer += 1

    return answer

people = [70, 80, 50]
limit = 100
print(solution(people, limit))