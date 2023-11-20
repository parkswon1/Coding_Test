T = int(input())

for test_case in range(1,T+1):
    numbers= list(map(int,input().split()))
    numbers.sort()

    low = numbers[0]
    big = numbers[-1]
    middle = 0
    middle_c = 0
    for n in numbers:
        if n != low and n != big:
            middle += n
            middle_c += 1

    print(f'#{test_case}',int(round(middle/middle_c,0)))