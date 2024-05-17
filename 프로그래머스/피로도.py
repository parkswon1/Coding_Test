def solution(k, d):
    global visit, dungeons

    dungeons = d
    visit = [False] * len(dungeons)

    recur(0, k)

    return ans

visit = []
dungeons = []
ans = 0

def recur(s, now):
    global ans
    if s == len(dungeons):
        ans = s
        return

    for i in range(len(dungeons)):
        if visit[i] == False and now >= dungeons[i][0]:
            visit[i] = True
            recur(s + 1, now - dungeons[i][1])
            visit[i] = False

    ans = max(ans, s)

k = 80
dungeons = 	[[80,20],[50,40],[30,10]]
print(solution(k, dungeons))