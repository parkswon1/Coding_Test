from collections import deque

def solution(info, edges):
    answer = 0
    dict = {}
    for i in range(len(info)):
        dict[i] = ([])
    for a,b in edges:
        dict[a].append(b)
    
    nodes = deque([(0,1,0,set())]) #지금노드, 양수, 늑대수, 방목할수있는 노드들
    while nodes:
        current, sC, wC, canVisit = nodes.popleft()
        answer = max(sC, answer)
        canVisit.update(dict[current])
        
        for next in canVisit:
            if info[next] == 1:
                if sC > wC + 1:
                    nodes.append((next, sC, wC + 1, canVisit - {next}))
            else:
                nodes.append((next, sC + 1, wC, canVisit - {next}))    
    
    return answer