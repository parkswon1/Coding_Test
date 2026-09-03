def solution(diff, times, limit):
    answer = 0
    front = 1
    back = 10**15
    while(front < back):
        time = times[0]
        level = (front + back)//2
        for i in range(1, len(diff)):
            if level >= diff[i]:
                time += times[i]
            else:
                c = diff[i] - level
                time += c * (times[i] + times[i - 1]) + times[i]
        if time > limit:
            front = level + 1
        else:
            back = level
    return front