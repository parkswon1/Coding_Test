import sys

N = int(sys.stdin.readline())
number = []
for n in range(N):
    num = int(sys.stdin.readline())
    number.append(num)

number.sort()
for n in number:
    print(n)