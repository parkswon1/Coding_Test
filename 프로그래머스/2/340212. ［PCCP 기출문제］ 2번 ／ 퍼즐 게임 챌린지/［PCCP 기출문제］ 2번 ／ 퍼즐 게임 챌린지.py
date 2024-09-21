def can_solve_with_level(level, diffs, times, limit):
    total_time = 0
    prev_time = 0

    for i in range(len(diffs)):
        if level >= diffs[i]:
            total_time += times[i]
        else:
            fail_count = diffs[i] - level
            total_time += times[i] + (times[i] + prev_time) * fail_count
        
        prev_time = times[i]
        if total_time > limit:
            return False
    
    return True

def solution(diffs, times, limit):
    low, high = 1, max(diffs)
    while low < high:
        mid = (low + high) // 2
        if can_solve_with_level(mid, diffs, times, limit):
            high = mid
        else:
            low = mid + 1
    return low