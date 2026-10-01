def solution(tickets):
    graph = {}

    for start, end in tickets:
        if start not in graph:
            graph[start] = []
        graph[start].append(end)

    for start in graph:
        graph[start].sort(reverse=True)

    stack = ["ICN"]
    answer = []

    while stack:
        node = stack[-1]
        
        if node in graph and graph[node]:
            nextNode = graph[node].pop()
            stack.append(nextNode)
        else:
            answer.append(stack.pop())


    return answer[::-1]