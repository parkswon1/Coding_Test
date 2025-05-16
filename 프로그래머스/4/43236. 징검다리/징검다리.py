def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    start = 1
    end = distance
    while start <= end:
        mid = (start + end) // 2

        prev = 0
        count = 0
        for r in rocks:
            if r - prev < mid:
                count += 1
            else:
                prev = r

        if count <= n:
            start = mid + 1
        else:
            end = mid - 1
    return start - 1