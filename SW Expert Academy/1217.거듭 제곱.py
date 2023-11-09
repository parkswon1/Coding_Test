def mix(a):
    global count
    a = a*N
    count += 1
    if count == M:
        return a
    else:
        return(mix(a))
    
for test_case in range(1,11):
    input()
    count = 1
    N,M = map(int,input().split())
    c = mix(N)
    print(f"#{test_case}",c)