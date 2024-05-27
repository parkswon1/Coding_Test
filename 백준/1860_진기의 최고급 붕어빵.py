T = int(input())

for test_case in range(1,T+1):
    N, M, K =map(int,input().split())
    customer = list(map(int,input().split()))

    customer.sort()
    bread = 0
    time = 0
    c_index = 0
    check = 0
    for i in range(0,11112):
        if i % M == 0 and i != 0:
            bread += K
        while(1):
            if c_index == N:
                break
            if customer[c_index] == i:
                if bread != 0:
                    bread -= 1
                else:
                    check =1
                c_index += 1
            else:
                break
    if check == 1:
        print(f'#{test_case}','Impossible')
    else:
        print(f'#{test_case}','Possible')

