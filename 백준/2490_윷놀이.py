for i in range(3):
    number = list(map(int,input().split()))
    nc = number.count(1)
    if nc == 4:
        print('E')
    elif nc == 1:
        print('C')
    elif nc == 2:
        print('B')
    elif nc == 3:
        print('A')
    elif nc == 0:
        print('D')