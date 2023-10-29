N = int(input())

numbers = []

for i in range(N):
    numbers.append(int(input()))

numbers.sort()

output = 0

while(1):
    a = numbers.pop()
    if len(numbers) == 0:
        output += a
        break
    if a <= 0:
        numbers.append(a)
        break
    else:
        b = numbers.pop()
        if b <= 0:
            output += a
            numbers.append(b)
            break
        output += max(a*b,a+b)
        if len(numbers) == 0:
            break
        
i = 0
lenth = len(numbers)
if lenth > 0:
    while(1):
        a = numbers[i]
        if i+1 >= lenth:
            output += a
            break
        else:
            i += 1
            b = numbers[i]
            output += (a*b)
            if i+1 >= lenth:
                break
            else:
                i += 1

print(output)