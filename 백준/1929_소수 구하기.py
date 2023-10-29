M, N = list(map(int, input().split()))
numbers=[]
    
for i in range(0,1000001):
    numbers.append(i)

numbers[1] = 0

for i in numbers:
    if i != 0:
        for j in range(2,1000000):
            if i * j > 1000000:
                break
            numbers[i*j] = 0

for i in range(M,N+1):
    if numbers[i] != 0:
        print(numbers[i])