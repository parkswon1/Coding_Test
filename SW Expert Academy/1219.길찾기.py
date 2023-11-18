def BFS(node):
    next_node = []
    for n in node:
        for k in range(1,len(nodes[n])):
            if nodes[n][k] == 99:
                print(f'#{test_case}',1)
                return
            next_node.append(nodes[n][k])
    if len(next_node) == 0:
        print(f'#{test_case}',0)
        return
    else:
        BFS(next_node)

for test_case in range(1,11):
    t,N = map(int,input().split())
    nodes = [[0]]*100
    line = list(map(int,input().split()))
    for i in range(0,N*2,2):
        nodes[line[i]] = nodes[line[i]]+[(line[i+1])]

    BFS([0])