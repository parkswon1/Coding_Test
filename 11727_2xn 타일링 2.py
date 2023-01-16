n = int(input())

n1 = 1
n2 = 1

for i in range(n-1):
    temp = n1 + n2*2
    n2 = n1
    n1 = temp
    
if n == 1:
    print(n1%10007)
else:
    print(temp%10007)