T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    output = []
    money = [50000,10000,5000,1000,500,100,50,10]

    for m in money:
        output.append(N // m)
        N = N % m

    print(f'#{test_case}')
    print(*output)