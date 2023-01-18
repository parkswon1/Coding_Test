N = int(input())

n1 = 1
n2 = 1
a = n1
b = n2

for i in range(N-2):
    temp = b + a
    a = b
    b = temp
    
if N == 1:
    print(n1)
elif N == 2:
    print(n2)
else:
    print(temp)