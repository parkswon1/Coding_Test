def solution(food):
    answer = ""
    backStack = []
    for i in range(1,len(food)):
        count = food[i]//2
        for j in range(count):
            answer += str(i)
            backStack.append(i)
    answer += "0"
    while(backStack):
        answer += str(backStack.pop())
    return answer

food = [1, 7, 1, 2]
print(solution(food))