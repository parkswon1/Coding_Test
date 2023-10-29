n,m = list(map(int,input().split()))

numbers = list(map(int,input().split()))

for k in range(m):
    numbers.sort()
    temp = numbers[0] + numbers[1]
    numbers[0] = temp
    numbers[1] = temp
        
print(sum(numbers))