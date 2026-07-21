import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0

    answer = 0
    dict = {}
    for w in works:
        if w in dict:
            dict[w] += 1
        else:
            dict[w] = 1
    wheap = []
    for i in dict:
        heapq.heappush(wheap, -i)
    
    while wheap:
        now = -heapq.heappop(wheap)
        nowCount = dict[now]
        diff = n - nowCount
        if diff < 0:
            dict[now] -= n
            if now - 1 in dict:
                dict[now - 1] += n
            else:
                dict[now - 1] = n
            heapq.heappush(wheap, - (now-1))
            break
        else:
            dict.pop(now)
            n -= nowCount
            if now - 1 in dict:
                dict[now - 1] += nowCount
            else:
                dict[now - 1] = nowCount
                heapq.heappush(wheap, -(now - 1))
                
            
    for i in dict:
        answer += (i*i) * dict[i]
    return answer