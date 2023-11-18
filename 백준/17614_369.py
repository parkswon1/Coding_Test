import sys
N = int(input())

output = 0
for n in range(1,N+1):
    numbers= str(n)
    output += numbers.count('3')
    output += numbers.count('6')
    output += numbers.count('9')
print(output)