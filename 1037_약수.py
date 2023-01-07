import sys
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
MAX = max(numbers)
MIN = min(numbers)
print(MAX*MIN)