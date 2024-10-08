def solution(picks, minerals):
    global answer, length
    answer = int(1e9)
    length = len(minerals)

    dfs(picks, 0, 0, minerals)

    return answer
def dfs(picks, index, result, minerals):
    global answer, length
    if picks == [0,0,0]:
        if answer > result:
            answer = result

    if picks[0] > 0:
        new_result = result
        for m in minerals[index:index + 5]:
            new_result += 1
        if index + 5 >= length:
            if answer > new_result:
                answer = new_result
        else:
            dfs([picks[0] - 1, picks[1], picks[2]], index + 5, new_result, minerals)

    if picks[1] > 0:
        new_result = result
        for m in minerals[index:index + 5]:
            if m == 'diamond':
                new_result += 5
            else:
                new_result += 1
        if index + 5 >= length:
            if answer > new_result:
                answer = new_result
        else:
            dfs([picks[0], picks[1] - 1, picks[2]], index + 5, new_result, minerals)

    if picks[2] > 0:
        new_result = result
        for m in minerals[index:index + 5]:
            if m == 'diamond':
                new_result += 25
            elif m == 'iron':
                new_result += 5
            else:
                new_result += 1
        if index + 5 >= length:
            if answer > new_result:
                answer = new_result
        else:
            dfs([picks[0], picks[1], picks[2] - 1], index + 5, new_result, minerals)

print(solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))