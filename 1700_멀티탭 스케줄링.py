import heapq
N, K = list(map(int,input().split()))

Elec = list(map(int,input().split()))

count  = [0] * 100
count[Elec[0]-1] = 1
for e in range(1,len(Elec)):
    if Elec[e] != Elec[e-1]: 
        count[Elec[e]-1] += 1

plug = []

Output = 0

for i in range(len(Elec)):
    if [count[Elec[i]-1],Elec[i]] not in plug:
        if len(plug) <= N:
            heapq.heappush(plug, [count[Elec[i]-1],Elec[i]])
        else:
            heapq.pop(plug)