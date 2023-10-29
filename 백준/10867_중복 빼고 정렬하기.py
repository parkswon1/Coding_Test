import sys
N = int(sys.stdin.readline())
number = sys.stdin.readline().split()
numberset = set(map(int,number))
number=list(numberset)
number.sort()

print(*number)