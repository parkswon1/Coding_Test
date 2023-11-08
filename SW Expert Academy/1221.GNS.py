T = input()
for test_case in range(1,11):
    input()
    num_str = list(input().split())
    
    c = [0]*10
    
    for n in num_str:
        if n == "ZRO":
            c[0] += 1
        elif n == "ONE":
            c[1] += 1
        elif n == "TWO":
            c[2] += 1
        elif n == "THR":
            c[3] += 1
        elif n == "FOR":
            c[4] += 1
        elif n == "FIV":
            c[5] += 1
        elif n == "SIX":
            c[6] += 1
        elif n == "SVN":
            c[7] += 1
        elif n == "EGT":
            c[8] += 1
        elif n == "NIN":
            c[9] += 1
    print(f"#{test_case}")
    print("ZRO "*c[0] + "ONE "*c[1] + "TWO "*c[2] + "THR "*c[3] + "FOR  "*c[4] + "FIV "*c[5] + "SIX "*c[6] + "SVN "*c[7] + "EGT "*c[8] + "NIN "*c[9])