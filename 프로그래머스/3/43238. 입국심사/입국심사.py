def solution(n, times):
    answer = 0
    front = 0
    end = max(times) * n
    while front < end:
        middle = (front + end)//2
        count = 0
        for t in times:
            count += middle//t
            
        if count >= n:
            end = middle
        else:
            front = middle + 1
    return front