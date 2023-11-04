T = 10
for test_case in range(1,T+1):
    number, right = input().split()
    output = []
    left = [right[0]]
    for r in range(1,int(number)):
        if len(left) != 0 and right[r] == left[-1]:
            left.pop()
        else:
            left.append(right[r])
        
    print(f'#{test_case}',int(''.join(left)))