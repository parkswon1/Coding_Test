def sol(n,r,c):
    if n==0:
        return 0
    return 2*(r%2)+(c%2) + 4*sol(n-1,int(r/2),int(c/2))

n,r,c=list(map(int,input().split()))

print(sol(n,r,c))