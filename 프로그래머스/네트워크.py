from collections import deque

def solution(N, computers):
    visited = [True] * (N)
    answer = 0
    for n in range(N):
        if visited[n]:
            visited[n] = False
            answer += 1
            nodes = deque([n])
            while nodes:
                node = nodes.popleft()
                for i in range(len(computers[node])):
                    if visited[i] and computers[node][i] == 1:
                        visited[i] = False
                        nodes.append(i)

    return answer

print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))