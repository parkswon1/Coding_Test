import sys
N = int(sys.stdin.readline())

numbers = 666
count = 0
while(1):
    if '666' in str(numbers):
        count += 1
        if count == N:
            print(numbers)
            break
    numbers += 1