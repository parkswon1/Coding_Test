import heapq

def solution(N, road, K):
    answer = 0
    visitCost = [float('inf')] * (N+1)
    costs = {}
    for a,b,c in road:
        if a not in costs:
            costs[a] = [(b,c)]
        else:
            costs[a].append((b,c))
        if b not in costs:
            costs[b] = [(a,c)]
        else:
            costs[b].append((a,c))
    
    nodes = []
    heapq.heappush(nodes, (0,1)) #거리 도시
    visitCost[1] = 0
    
    while(nodes):
        currentCost, node = heapq.heappop(nodes)
        for nextNode, cost in costs[node]:
            if currentCost + cost < visitCost[nextNode] and currentCost + cost <= K:
                visitCost[nextNode] = currentCost + cost
                heapq.heappush(nodes, (visitCost[nextNode], nextNode))
    for v in visitCost:
        if v <= K:
            answer += 1

    return answer