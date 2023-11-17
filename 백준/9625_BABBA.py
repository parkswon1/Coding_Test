K = int(input())
A = [0,1]
B = [1,1]
if K == 1:
    print(*[0,1])
else:
    for k in range(1,K-1):
        A[0], A[1] = A[1] , A[0] + A[1]
        B[0], B[1] = B[1] , B[0] + B[1]
    print(A[1],B[1])