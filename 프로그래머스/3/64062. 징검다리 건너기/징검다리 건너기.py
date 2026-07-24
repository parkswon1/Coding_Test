def solution(stones, k):
    answer = 0
    front = 0
    end = max(stones)
    while front < end:
        middle = (front + end)//2
        zcount = 0
        for stone in stones:
            if stone <= middle:
                zcount += 1
                if zcount == k:
                    break
            else:
                zcount = 0
        
        if zcount == k:
            end = middle
        else:
            front = middle + 1
        
    return front