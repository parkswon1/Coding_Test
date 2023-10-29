n = int(input())
a = 1
b = 1
c = 1
for i in range(1,n):
    temp = a+b+c
    k = a + b
    m = a + c
    a = temp
    b = k
    c = m

print((a+b+c)%9901)