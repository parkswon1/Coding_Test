from collections import defaultdict
import heapq

def solution(N, roads, K):
    answer = 0
    nodes = defaultdict(list)
    for x, y, z in roads:
        nodes[x].append([y, z])
        nodes[y].append([x, z])
    
    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    
    q = [(0,1)]
    
    while q:
        d, curr = heapq.heappop(q)
        
        if dist[curr] < d:
            continue
        
        for nxt, w in nodes[curr]:
            cost = d + w
            if cost < dist[nxt]:
                dist[nxt] = cost
                heapq.heappush(q, (cost, nxt))
        

    return len([i for i in dist if i <= K])