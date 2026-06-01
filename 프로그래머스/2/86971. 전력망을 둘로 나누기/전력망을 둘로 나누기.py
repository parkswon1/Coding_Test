from collections import deque

def bfs(N, wires):
    visited = set()
    
    dict = {}
    for a,b in wires:
        if a == 0:
            continue
        if a in dict:
            dict[a].append(b)
        else:
            dict[a] = [b]
        if b in dict:
            dict[b].append(a)
        else:
            dict[b] = [a]
            
    counts = []
    for n in range(1, N + 1):
        if n in visited:
            continue
        nodes = deque([n])
        count = 1
        visited.add(n)
        
        while(nodes):
            node = nodes.popleft()
            if node not in dict:
                visited.add(node)
                continue
            for nextNode in dict[node]:
                if nextNode in visited:
                    continue
                nodes.append(nextNode)
                visited.add(nextNode)
                count += 1

        counts.append(count)
    return counts

def solution(n, wires):
    answer = float('inf')
    
    for i in range(len(wires)):
        a, b = wires[i]
        wires[i] = [0,0]
        x, y = bfs(n, wires)
        answer = min(answer,abs(x-y))
        wires[i] = [a,b]
        
    return answer