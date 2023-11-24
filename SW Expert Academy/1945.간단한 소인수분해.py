T=  int(input())

for test_case in range(1,T+1):
    N = int(input())
    A = [2,3,5,7,11]
    output = [0,0,0,0,0]
    for a in range(5):
        while(1):
            if N % A[a] != 0:
                break
            N = N/A[a]
            output[a] += 1
    print(f'#{test_case}', *output)