T = int(input())
for i in range(T):
    n = int(input())
    node =[0]*(n)
    node[0]=1
    if n >= 2:
        node[1]=2
    if n >= 3:
        node[2]=4
    for j in range(3,n):
        node[j]=node[j-3]+node[j-2]+node[j-1]
    print(node[n-1])