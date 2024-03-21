def solution(n):
    hano(n,1,3,2)

def hano(num, now, to, ex):
    global count
    if num == 1:
        count += 1
        answer.append([now,to])
        return

    hano(num-1, now, ex, to)
    count += 1
    answer.append([now,to])
    hano(num-1, ex, to, now)

answer = []
n = int(input())
count = 0
solution(n)

print(count)
for a in answer:
    print(*a)
