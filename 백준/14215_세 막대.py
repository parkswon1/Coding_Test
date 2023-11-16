numbers = list(map(int,input().split()))

numbers.sort()

if numbers[0] + numbers[1] <= numbers[2]:
    numbers[2] = numbers[0] + numbers[1] - 1

print(sum(numbers))