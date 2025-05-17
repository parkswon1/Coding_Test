def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers, target, -numbers[0], 1)
    dfs(numbers, target, numbers[0], 1)    
    return answer


def dfs(numbers, target, count, index):
    global answer
    if index == len(numbers):
        if count == target:
            answer += 1
    
    else:
        dfs(numbers, target, count + numbers[index], index + 1)
        dfs(numbers, target, count - numbers[index], index + 1)
    