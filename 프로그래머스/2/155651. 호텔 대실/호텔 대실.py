import heapq

def solution(book_time):
    answer = 0
    
    #룸예약수를 잡아놀 힙큐
    roomHeap = []
    
    book_time.sort()
    
    for book in book_time:
        
        #기존 만료된 방 제거
        while(roomHeap):
            if roomHeap[0] <= book[0]:
                heapq.heappop(roomHeap)
            else:
                break
        
        heapq.heappush(roomHeap, add10min(book[1]))
        answer = max(len(roomHeap), answer)
    
    return answer

def add10min(time):
    h, m = map(int, time.split(":"))
    m += 10
    if m >= 60:
        if h < 23:
            h += 1  
            m -= 60
    return f"{h:02d}:{m:02d}"