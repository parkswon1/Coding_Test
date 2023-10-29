import sys
sys.setrecursionlimit(10**6)

def dfs(Fn_2,Fn_1):
    global count 
    Fn = Fn_2 + Fn_1
    count += 1
    if count == N:
        print(Fn)
        return
    else:
        dfs(Fn_1, Fn)

N = int(input())
F0 = 0
F1 = 1
count = 1
if N == 1:
    print(1)
else:
    dfs(F0,F1)
