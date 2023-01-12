import sys
N = int(input())
xy =[]
for i in range(N):
    a,b = list(map(int,sys.stdin.readline().split()))
    xy.append([b,a])
    
xy.sort()   

for i in xy:
    print(i[1],i[0])