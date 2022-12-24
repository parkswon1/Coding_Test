N = int(input())
A = list(map(int,input().split()))
B, C =map(int,input().split())
low =0
for i in range(len(A)):
    low = low+1
    if A[i] > B :
        number= A[i]-B
        a = number%C
        low += number//C
        if a != 0:
            low +=1

print(low)
        