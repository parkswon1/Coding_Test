import heapq

def solution(book_time):
    answer = 0
    
    rooms = []
    for b in book_time:
        heapq.heappush(rooms, (converTime(b[0]), converTime(b[1])))
    
    usingR = []
    while rooms:
        r = heapq.heappop(rooms)
        heapq.heappush(usingR, r[1])
        while usingR:
            if usingR[0] + 10 <= r[0]:
                heapq.heappop(usingR)
            else:
                break
        answer = max(len(usingR), answer)
        
    
    return answer

def converTime(s):
    h, s = map(int, s.split(":"))
    s += h * 60
    return s