import sys
N = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))

count = [1]*(N)
Min = numbers[0]

for i in range(N):
    for j in range(i):
        if numbers[j] < numbers[i]:
            count[i] = max(count[i],count[j]+1)
            
print(max(count))