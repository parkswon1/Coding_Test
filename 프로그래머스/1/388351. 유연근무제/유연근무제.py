def solution(schedules, timelogs, startday):
    answer = 0

    for i in range(len(timelogs)):
        cnt=0
        for j in range(7):
            if startday+j == 6 or startday+j == 7:
                continue
            hour = schedules[i] // 100
            minute = schedules[i] % 100 + 10
            if minute >= 60:
                hour += 1
                minute -= 60
            deadline = hour * 100 + minute
            if timelogs[i][j] > deadline:
                break
            else:
                cnt+=1
            if cnt==5:
                answer+=1
                
    return answer