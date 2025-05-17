import heapq

def solution(n, t, m, timetable):
    times = []
    for T in timetable:
        hour, mini = map(int, T.split(":"))
        heapq.heappush(times, hour * 60 + mini)
    
    suttles = [540]
    for i in range(1, n):
        suttles.append(suttles[-1] + t)
    
    # 마지막 셔틀 전까지 처리
    for suttle in suttles[:-1]:
        count = 0
        while times and times[0] <= suttle and count < m:
            heapq.heappop(times)
            count += 1

    # 마지막 셔틀만 따로 처리
    last_suttle = suttles[-1]
    count = 0
    last_crew = []
    while times and times[0] <= last_suttle and count < m:
        last_crew.append(heapq.heappop(times))
        count += 1

    if count < m:
        arrive = last_suttle
    else:
        arrive = last_crew[-1] - 1

    return f"{arrive // 60:02d}:{arrive % 60:02d}"