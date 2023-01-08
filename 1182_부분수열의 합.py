import sys

def dfs(index,Scount):
    global count
    if Scount == S:
        count +=1 
    if index+1 < N:
        dfs(index+1,Scount)
        dfs(index+1,Scount =integer[index]+Scount)
        
N, S = list(map(int, sys.stdin.readline().split()))
integer = list(map(int,sys.stdin.readline().split()))
count = 0
for i in range(N):
    dfs(i,integer[i])
print(count)