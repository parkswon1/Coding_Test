import sys
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
Mlist = list(map(int,sys.stdin.readline().split()))
A.sort()

for i in Mlist:
    left,right,check = 0, N-1, 0
    while(left <= right):
        mid = int((left+right)/2)
        if i == A[mid] :
            print(1)
            check = 1
            break
        elif i < A[mid]:
            right =mid-1
        else:
            left =mid+1
    if check == 0:
        print(0)