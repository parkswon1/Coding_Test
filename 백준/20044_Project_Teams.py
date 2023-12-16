import sys

N = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))

numbers.sort()

output = float('inf')
for n in range(N):
    output = min(numbers[n]+numbers[-n-1],output)

print(output)