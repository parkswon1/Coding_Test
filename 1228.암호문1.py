for test_case in range(1,11):
    input()
    pw = input().split()
    input()
    order = input().split()
    o_N = len(order)
    
    for o in range(o_N):
        if order[o] == "I":
            x = int(order[o+1])
            y = int(order[o+2])
            for i in range(y):
                pw.insert(x+i,order[o + i + 3])
         
    print(f"#{test_case}",*pw[:10])