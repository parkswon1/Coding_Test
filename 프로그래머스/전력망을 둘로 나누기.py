from collections import deque

def solution(n, wires):
    answer = float('inf')
    for i in range(len(wires)):
        a = wires[i][0]
        b = wires[i][1]
        wires[i][0] = 0
        wires[i][1] = 0
        answer = min(search(n, wires),answer)
        wires[i][0] = a
        wires[i][1] = b

    return answer

def search(n, wires):
    dict = {}
    for wire in wires:
        if wire[0] not in dict:
            dict[wire[0]] = [wire[1]]
        else:
            dict[wire[0]] += [wire[1]]
        if wire[1] not in dict:
            dict[wire[1]] = [wire[0]]
        else:
            dict[wire[1]] += [wire[0]]

    visited = set()
    count = [0,0]
    index = -1
    for i in range(1,n + 1):
        if i not in visited:
            index += 1
            count[index] += 1
            visited.add(i)
            nodes = deque([i])
            while(nodes):
                node = nodes.popleft()
                if node in dict:
                    for d in dict[node]:
                        if d not in visited:
                            count[index] += 1
                            visited.add(d)
                            nodes.append(d)

    return abs(count[0] - count[1])

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n, wires))