import sys

def dfs(index,Scount):
    global count
    if index == N:
        if Scount == S:
            count +=1
        return
    dfs(index+1,Scount)
    dfs(index+1,Scount =integer[index]+Scount)
        
N, S = list(map(int, sys.stdin.readline().split()))
integer = list(map(int,sys.stdin.readline().split()))
count = 0
dfs(0,0)
if S == 0:
    count -=1
print(count)