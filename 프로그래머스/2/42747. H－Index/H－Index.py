def solution(citations):
    answer = 0
    N = len(citations)
    citations.sort()
    for i in range(N):
        if citations[i] >= N - i:
            return N - i
    return answer