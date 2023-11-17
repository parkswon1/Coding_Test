def can(n,x,y):
    if n < 1:
        return
    can(int(n/3),x,x+n)
    can(int(n/3),y-n,y)
    for i in range(x+n,y-n):
        arr[i] = ' '
while True:
    try:
        N = int(input())
        dis = 3**N
        arr = ['-']*(dis)
        can(int(dis/3),0,dis)
        print(''.join(arr))
    except:
        break