import heapq

def solution(n, costs):
    answer = 0
    dict = {} #key는 노드, (도착지, cost)
    for a,b,c in costs:
        if a not in dict:
            dict[a] = [(b,c)]
        else:
            dict[a].append((b,c))
        if b not in dict:
             dict[b] = [(a,c)]
        else:
            dict[b].append((a,c))
    
    visited = set()
    nodes = [(0,0)]
    heapq.heapify(nodes) #cost, 지금노드
    while nodes:
        cost, node = heapq.heappop(nodes)
        if node in visited:
            continue
        
        visited.add(node)
        answer += cost
        
        for nextNode, nextCost in dict[node]:
            if nextNode not in visited:
                heapq.heappush(nodes, (nextCost, nextNode))
            
            
    
    
    return answer 