T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    output = 0
    for n in range(1,N+1):
        if n % 2 == 0:
            output -= n
        else:
            output += n

    print(f'#{test_case}',output)