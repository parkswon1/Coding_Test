import sys
Case = int(input())
for i in range(Case):
    N, M = list(map(int, sys.stdin.readline().split()))
    doclist = list(map(int, sys.stdin.readline().split()))
    count = 0
    MAX = max(doclist)
    index = 0
    for j in doclist:
        if index == M:
            if MAX == j:
                count +=1
                print(count)
                break
            else:
                doclist.append(j)
                M = len(doclist)-1
        else:
            if j < MAX:
                doclist.append(j)
                doclist[index] = 0
            else:
                count +=1
                doclist[index] = 0
                MAX = max(doclist)
        index +=1
