def solution(n, times):
    start = 1
    end = min(times) * n
    
    while start <= end:
        mid = (start + end) // 2
        
        
        count = 0
        for t in times:
            count += mid // t
        
        if n > count:
            start = mid + 1
        else:
            end = mid - 1
        
    return start