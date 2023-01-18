N = int(input())
numbers = list(map(int,input().split()))

pluses = [0]*N
pluses[0] = numbers[0]
for i in range(1,N):
    pluses[i] = max(pluses[i-1]+numbers[i],numbers[i])

print(max(pluses))