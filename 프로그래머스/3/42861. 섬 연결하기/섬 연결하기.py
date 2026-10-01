import heapq

def solution(n, costs):
    answer = 0
    dict = {}
    for a,b,c in costs: #a노드 b노드 c가격
        if a not in dict:
            dict[a] = [(b,c)] 
        else:
            dict[a].append((b,c))
        
        if b not in dict:
            dict[b] = [(a,c)]
        else:
            dict[b].append((a,c))
            
    nodes = []
    heapq.heappush(nodes, (0,0)) #간선 비용, 다음노드
    visited = set()
    while nodes:
        cost, node = heapq.heappop(nodes)
        if node in visited:
            continue
        
        visited.add(node)
        answer += cost
        for a, c in dict[node]:
            if a in visited:
                continue
            heapq.heappush(nodes, (c, a))
    
    return answer