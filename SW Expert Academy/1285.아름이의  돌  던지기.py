T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    count = [0]*100001
    numbers = list(map(int,input().split()))
    for n in numbers:
        if n < 0 :
            count[-n] += 1
        else:
            count[n] += 1

    for c in range(100001):
        if count[c] != 0:
            print(f'#{test_case}', c, count[c])
            break