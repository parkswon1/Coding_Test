def solution(k, dungeons):
    answer = -1
    stack = [(k, set())] #남은 피로도, 방문기록
    while stack:
        k, visited = stack.pop()
        
        for i in range(len(dungeons)):
            if i in visited:
                continue

            limit, dk = dungeons[i]
            if k < limit:
                continue
            
            answer = max(len(visited) + 1, answer)
            stack.append((k - dk, visited | {i}))
    return answer