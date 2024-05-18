from collections import deque

dict = {}

def solution(n, edge):
    answer = 0
    logDistance = 0

    for e in edge:
        dictcontroll(e[0], e[1])

    visited = set()
    nodes = deque([[1,0]])
    visited.add(1)
    while(nodes):
        node = nodes.popleft()
        for nextnode in dict[node[0]]:
            if nextnode not in visited:
                visited.add(nextnode)
                if logDistance < node[1] + 1:
                    logDistance = node[1] + 1
                    answer = 1
                elif logDistance == node[1] + 1 :
                    answer += 1
                nodes.append([nextnode,node[1] + 1])

    return answer

def dictcontroll(v1, v2):
    global dict
    if v1 in dict:
        dict[v1].append(v2)
    else:
        dict[v1] = [v2]
    if v2 in dict:
        dict[v2].append(v1)
    else:
        dict[v2] = [v1]



n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))