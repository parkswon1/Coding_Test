def solution(k, dungeons):
    answer = -1
    nodes = [(k,set())] #피로도, 방문한 던전
    
    while(nodes):
        fatigue, visited = nodes.pop()
        for i in range(len(dungeons)):
            if i in visited or dungeons[i][0] > fatigue:
                continue
            
            answer = max(answer, len(visited) + 1)
            nodes.append((fatigue - dungeons[i][1], visited | {i}))
            
    
    
    
    return answer