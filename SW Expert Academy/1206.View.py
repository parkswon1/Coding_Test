for test_case in range(1,11):
    N = int(input())
    tower = list(map(int,input().split()))
    output = 0
    for n in range(2,N-2):
        minus = tower[n] - max(tower[n-2],tower[n-1],tower[n+1],tower[n+2]) 
        if minus >= 1:
            output += minus
    
    print(f"#{test_case}",output)