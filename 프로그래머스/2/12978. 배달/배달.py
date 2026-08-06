import heapq

def solution(N, road, K):
    answer = 0
    rdict = {}
    for a,b,c in road:
        if a not in rdict:
            rdict[a] = [(b,c)]
        else:
            rdict[a].append((b,c))
        if b not in rdict:
            rdict[b] = [(a,c)]
        else:
            rdict[b].append((a,c))
    
    nodes = []
    heapq.heappush(nodes,(0,1)) #cost, 노드번호
    visited = {}
    visited[1] = 0
    while nodes:
        cost, node = heapq.heappop(nodes)
        if cost > visited[node]:
            continue
            
        for nnode, ncost in rdict[node]:
            if ncost + cost > K:
                continue
            if nnode not in visited or visited[nnode] > cost + ncost:
                visited[nnode] = cost + ncost
                heapq.heappush(nodes, (cost+ncost, nnode))
    
    return len(visited)
