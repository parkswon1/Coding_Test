import heapq

def solution(n, costs):
    answer = 0
    dict = {}
    for a,b,c in costs:
        if a in dict:
            dict[a].append((b,c))
        else:
            dict[a] = [(b,c)]
        if b in dict:
            dict[b].append((a,c))
        else:
            dict[b] = [(a,c)]
    
    nodes = []
    heapq.heappush(nodes, (0,0)) #cost, node 번호
    visited=set()
    
    while nodes:
        temp, currentnode = heapq.heappop(nodes)
        if currentnode in visited:
            continue
        else:
            visited.add(currentnode)
        answer += temp
        
        for node, cost in dict[currentnode]:
            if node not in visited:
                heapq.heappush(nodes,(cost, node))
        
    
    return answer