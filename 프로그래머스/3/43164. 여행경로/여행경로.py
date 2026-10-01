def solution(tickets):
    graph = {}

    for start, end in tickets:
        if start not in graph:
            graph[start] = []
        graph[start].append(end)

    # pop()으로 알파벳이 작은 공항부터 꺼내기 위해 역순 정렬
    for start in graph:
        graph[start].sort(reverse=True)

    stack = ["ICN"]
    answer = []

    while stack:
        now = stack[-1]

        # 아직 사용할 티켓이 있으면 이동
        if now in graph and graph[now]:
            nextNode = graph[now].pop()
            stack.append(nextNode)

        # 더 이상 갈 곳이 없으면 그 공항을 경로에 확정
        else:
            answer.append(stack.pop())

    return answer[::-1]