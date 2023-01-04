import sys
N = int(input())
char =[]
for i in range(N):
    a,b = list(map(int,sys.stdin.readline().split()))
    char.append([b,a])
    
char.sort()   

for i in char:
    print(i[1],i[0])