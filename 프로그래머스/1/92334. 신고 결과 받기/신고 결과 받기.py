def solution(id_list, report, k):
    answer = []
    whoDict = {}
    reportedCount = {}
    stop = set()
    for r in report:
        who, reported = r.split(" ")
        if who in whoDict and reported in whoDict[who]:
            continue
            
        reportedCount[reported] = reportedCount.get(reported, 0) + 1
        if reportedCount[reported] >= k:
            stop.add(reported)
        
        if who not in whoDict:
            whoDict[who] = set([reported])
        else:
            whoDict[who].add(reported)
    
    for id in id_list:
        count = 0
        if id in whoDict:
            for w in whoDict[id]:
                if w in stop:
                    count += 1
        answer.append(count)
    
    return answer