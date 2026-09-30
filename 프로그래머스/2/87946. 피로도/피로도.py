def solution(k, dungeons):
    answer = -1
    nodes = [(k, set())] #피로도, 방문기록
    while nodes:
        k, visited = nodes.pop()
        for i in range(len(dungeons)):
            if i in visited:
                continue
            
            if dungeons[i][0] <= k:
                answer = max(answer, len(visited) + 1)
                nodes.append((k - dungeons[i][1], visited | {i}))
    
    return answer