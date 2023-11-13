for test_case in range(1,11):
    test_case = int(input())
    boxs = []
    last_box = []

    for i in range(100):
        boxs.append(list(map(int,input().split())) + [0])
            
        
    boxs.append([0]*101)
    right = 0
    left = 0
    for y in range(100):
        for x in range(100):
            boxs[y][100] += boxs[y][x]
            boxs[100][x] += boxs[y][x]
            if  y == x:
                right += boxs[y][x]
            if  y + x == 100:
                left += boxs[y][x]
                
        last_box.append(boxs[y][100])
        
    last_box += boxs[100] + [right] + [left]
    print(f'#{test_case}',max(last_box))