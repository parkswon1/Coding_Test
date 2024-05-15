import heapq
def solution(jobs):
    jobs.sort()
    n = len(jobs)
    heap = []
    now = ans = 0
    while jobs or heap:
        while jobs and now >= jobs[0][0]:
            heapq.heappush(heap,jobs.pop(0)[::-1])
        if jobs and not heap:
            i = jobs.pop(0)
            now = i[0]
            heapq.heappush(heap, i[::-1])
        j = heapq.heappop(heap)
        now += j[0]
        ans += now-j[-1]
    return ans//n

jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))