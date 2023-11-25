T=  int(input())

for test_case in range(1,T+1):
    Ah, Am, Bh, Bm = map(int,input().split())
    h = Ah + Bh
    m = Am + Bm
    if m >= 60:
        h += 1
        m = m - 60
    print(h)
    if h > 12:
        h = h - 12
    print(f'#{test_case}',h,m)