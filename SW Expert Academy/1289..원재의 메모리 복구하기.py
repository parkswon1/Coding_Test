T = int(input())

for test_case in range(1, T + 1):
    rem = input()
    
    bit = 0
    count = 0
    for r in range(len(rem)):
        if bit != int(rem[r]):
            count += 1
            bit = int(rem[r])
    
    print(f'#{test_case}',count)