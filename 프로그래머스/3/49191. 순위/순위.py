from collections import deque

def solution(n, results):
    winGraph = [[] for _ in range(n)]
    loseGraph = [[] for _ in range(n)]

    for winner, loser in results:
        winGraph[winner - 1].append(loser - 1)
        loseGraph[loser - 1].append(winner - 1)

    def bfs(start, graph):
        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()

            for nextNode in graph[node]:
                if nextNode in visited:
                    continue

                visited.add(nextNode)
                queue.append(nextNode)

        return len(visited)

    answer = 0

    for i in range(n):
        winCount = bfs(i, winGraph)
        loseCount = bfs(i, loseGraph)

        if winCount + loseCount == n - 1:
            answer += 1

    return answer