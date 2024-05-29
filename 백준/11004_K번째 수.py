import sys

N, K = map(int, input().split())
numbers = list(map(int,sys.stdin.readline().split()))

numbers.sort()
print(numbers[K - 1])