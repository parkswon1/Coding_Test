N, M = map(int,input().split())

basket = []
for n in range(1,N+1):
    basket.append(n)

for m in range(M):
    a,b = map(int,input().split())
    basket[a-1],basket[b-1] = basket[b-1],basket[a-1]

print(*basket)