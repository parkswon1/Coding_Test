for test_case in range(1,11):
    numbers = list(map(int,input().split()))
    
    minus = 1
    i = 0
    cycle = 0
    while(1):
        numbers[i] -= minus
        if numbers[i] <= 0:
            numbers[i] = 0
            break
        i += 1
        minus += 1
        cycle += 1
        if cycle == 5:
            minus = 1
            cycle = 0
        if i == 8:
            i = 0
        
    output =  numbers[i+1:] +numbers[:i+1]
    print(f"#{test_case}", *output)