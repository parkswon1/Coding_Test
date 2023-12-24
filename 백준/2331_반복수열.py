visit = [0]*300000
D = [0]
D[0], A= input().split()
A = int(A)
visit[int(D[0])] = 1
count = 1
while(1):
    nowD = D.pop()
    nextD = 0
    for d in nowD:
        nextD += int(d)**A
    if visit[nextD] == 0:
        count += 1
        visit[nextD] = count
        D.append(str(nextD))
    else:
        print(visit[nextD]-1)
        break