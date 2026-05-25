from collections import deque

def solution(info, edges):
    answer = 0
    dict = {}
    for i in range(len(info)):
        dict[i] = ([]) #(아래 간선)
    for a,b in edges:
        dict[a].append(b)
    
    nodes = deque([(0,1,0,set())]) #(노드번호, 양 수, 늑대 수, 방문 기록)
    
    while nodes:
        current, sheepCount, wolfCount, visited = nodes.popleft()
        answer = max(answer, sheepCount)
        visited.update(dict[current])
        
        for next in visited:
            if info[next]:
                if sheepCount > wolfCount + 1:
                    nodes.append((next, sheepCount, wolfCount + 1, visited - {next}))
            else:
                nodes.append((next, sheepCount + 1, wolfCount, visited - {next}))
                    
    
    return answer 