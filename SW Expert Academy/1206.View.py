test_case = int(input())

N = int(input())

hight = list(map(int,input().split()))
count = 0

for h in range(2,N-2):
    dif = hight[h] - max(hight[h-2],hight[h-1],hight[h+1],hight[h+2])
    if dif >= 1:
        count += dif
    
print(f'#{test_case}',count)