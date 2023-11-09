for test_case in range(1,11):
    input()
    magnetic = [0]*100
    output = 0
    for i in range(100):
        line = list(input().split())
        for l in range(100):
            if line[l] == '1':
                magnetic[l] = '1'
            elif line[l] == '2':
                if magnetic[l] == '1':
                    output += 1
                    magnetic[l] = '2'
                    
    print(f"#{test_case}",output)
    