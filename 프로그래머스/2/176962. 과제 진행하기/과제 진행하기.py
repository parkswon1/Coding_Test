def solution(plans):
    answer = []
    plans.sort(key=lambda x: x[1])

    stack = []
    nowTime = 0

    for name, start, playtime in plans:
        start = calTime(start)
        playtime = int(playtime)

        while stack:
            if stack[-1][0] <= start - nowTime:
                time, endname = stack.pop()
                answer.append(endname)
                nowTime += time
            else:
                stack[-1][0] -= start - nowTime
                nowTime = start
                break

        stack.append([playtime, name])
        nowTime = start

    while stack:
        time, name = stack.pop()
        answer.append(name)

    return answer

def calTime(time):
    hour, minite = time.split(":")
    return int(minite) + (int(hour) * 60)