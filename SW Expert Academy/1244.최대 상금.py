T = int(input())
for test_case in range(1,T+1):
    numbers, coin = input().split()
    coin = int(coin)
    
    before = set([numbers])
    after = set()

    for c in range(coin):
        while before:
            b = list(before.pop())
            for i in range(len(b)):
                for j in range(i+1,len(b)):
                    b[i], b[j] = b[j], b[i]
                    after.add(''.join(b))
                    b[i], b[j] = b[j], b[i]
        before, after = after, before
            
        
    print(f'#{test_case}', max(map(int,before)))