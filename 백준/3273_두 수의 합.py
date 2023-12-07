import sys

n = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
x = int(sys.stdin.readline())

count = 0
front = 0
numbers.sort()
back = n-1
while(1):
    number = numbers[front] + numbers[back]
    if number == x:
        count += 1
        back -= 1
        front += 1
    elif number > x:
        back -= 1
    else:
        front += 1

    if back - front <= 0:
        break
print(count)