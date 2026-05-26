import heapq

def solution(n, costs):
    answer = 0
    visited = set()
    nodes = []
    heapq.heappush(nodes, (0, 0)) #cost, nextNode
    dict = {}
    for start, end, cost in costs:
        if start in dict:
            dict[start].append((end, cost))
        else:
            dict[start] = [(end, cost)]
        if end in dict:
            dict[end].append((start,cost))
        else:
            dict[end] = [(start,cost)]
    
    while(nodes):
        cost, current = heapq.heappop(nodes)
        if current in visited:
            continue
        
        visited.add(current)
        answer += cost
        
        for nextNode, cost in dict[current]:
            heapq.heappush(nodes,(cost, nextNode))
        
    return answer