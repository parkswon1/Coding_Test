n = int(input())
a,b = map(int, input().split())
cus = []
visit = [0]*(n+1)
for i in range(n+1):
    cus.append([])
m = int(input())
for i in range(m):
    c,d = map(int, input().split())
    cus[c].append(d)
    cus[d].append(c)

count = 0
check=0
deep =[[a]]
visit[a]=1
for i in deep:
    count +=1
    node = []
    for k in i:
        for j in cus[k]:
            if j == b:
                print(count)
                check =1
                break
            if visit[j] == 0:
                visit[j] = 1
                node.append(j)   
    if len(node)==0:
        break
    deep.append(node)
if check ==0:
    print(-1)