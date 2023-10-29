T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    Dump = int(input())
    
    Boxs = [0]*101
    
    low_box = 0
    max_box = 100
    
    input_box = map(int, input().split())
    for i in input_box:
        Boxs[i] += 1
    
    for d in range(Dump):
        if Boxs[max_box] == 0:
            while(Boxs[max_box] == 0):
                max_box -= 1
        if Boxs[low_box] == 0:
            while(Boxs[low_box] == 0):
                low_box += 1
        Boxs[max_box] = Boxs[max_box] - 1
        Boxs[max_box-1] += 1
        Boxs[low_box] = Boxs[low_box] - 1
        Boxs[low_box+1] += 1
    
    if Boxs[max_box] == 0:
        max_box -= 1
    if Boxs[low_box] == 0:
        low_box += 1
    print(f'#{test_case}',max_box - low_box)