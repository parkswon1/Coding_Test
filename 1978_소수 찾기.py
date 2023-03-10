import sys
N = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))
count = 0 
for number in numbers:
    check = 0
    if number == 2:
        count +=1
    if number != 1:
        if number%2 != 0:
            for j in range(3,number-1,2):
                if number%j == 0:
                    check = 1
                    break
            if check == 0:
                count +=1
print(count)