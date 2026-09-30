import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    s = 0
    while len(scoville) > 1 and scoville[0] < K:
        s = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, s)
        answer += 1
    if scoville[0] < K :
        return -1
    return answer