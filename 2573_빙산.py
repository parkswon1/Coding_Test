def DFS(Node):
    global Year
    if len(Node) == 0:
        print(0)
        return
    for n in range(N):
       







N, M = list(map(int,input().split()))

Map = []
Count_Map = []
Ice_Mountains = []
Year = 0
for n in range(N):
    Count_Map.append([0]*M)
    Line = list(map(int,input().split()))
    for m in range(M):
        if Line[m] != 0:
            Ice_Mountains.append([n,m])
            Count_Map[n][m] = 1
            
    Map.append(Line)