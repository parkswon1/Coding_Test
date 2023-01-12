import sys
N = int(input())
xy =[]
for i in range(N):
    a,b = sys.stdin.readline().split()
    xy.append([a,b])
    
xy.sort()   

for i in xy:
    print(i[0],i[1])