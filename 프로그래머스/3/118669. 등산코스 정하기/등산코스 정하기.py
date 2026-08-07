import heapq 

def solution(n, paths, gates, summits):
    answer = [float('inf'), float('inf')]
    pdict = {}
    for a,b, cost in paths:
        if a not in pdict:
            pdict[a] = [(b,cost)]
        else:
            pdict[a].append((b,cost))
        if b not in pdict:
            pdict[b] = [(a,cost)]
        else:
            pdict[b].append((a,cost))
            
    nodes = []
    summits = set(summits)
    vdict = set()

    for g in gates:
        heapq.heappush(nodes, (0,g))
        
    while nodes:
        cost, node = heapq.heappop(nodes)
        if node in vdict:
            continue
        vdict.add(node)

        if node in summits:
            if cost < answer[1]:
                answer = [node, cost]
            elif cost == answer[1] and node < answer[0]:
                answer = [node, cost]
            continue 

        for nextnode, ncost in pdict.get(node, []):
            heapq.heappush(nodes, (max(cost, ncost), nextnode))
            
    return answer