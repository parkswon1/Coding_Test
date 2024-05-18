def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers[0], 1, numbers, target)
    dfs(-numbers[0], 1, numbers, target)
    return answer

def dfs(num, index, numbers, target):
    global answer
    if index == len(numbers):
        if num == target:
            answer += 1
    else:
        dfs(num + numbers[index], index + 1, numbers, target)
        dfs(num - numbers[index], index + 1, numbers, target)

print(solution([1,1,1,1,1],3))
print(solution([4,1,2,1],4))