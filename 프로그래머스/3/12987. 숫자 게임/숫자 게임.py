import heapq

def solution(A, B):
    answer = 0
    A.sort()
    heapq.heapify(B)
    for a in A:
        while B:
            if heapq.heappop(B) > a:
                answer +=1
                break
    return answer