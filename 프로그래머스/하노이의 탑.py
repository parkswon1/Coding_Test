def solution(n):
    hano(n,1,3,2)
    return answer

def hano(num, now, to, ex):
    if num == 1:
        answer.append([now,to])
        return

    hano(num-1, now, ex, to)
    answer.append([now,to])
    hano(num-1, ex, to, now)

n = 2
answer = []
print(solution(n))
