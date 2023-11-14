T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    price = list(map(int,input().split()))

    output = 0
    high_price = price[-1]

    for n in range(-1,-N-1,-1):
        if price[n] <= high_price:
            output += high_price - price[n]
        else:
            high_price = price[n]

    print(f'#{test_case}', output)