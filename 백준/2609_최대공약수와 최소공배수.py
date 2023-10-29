A, B = list(map(int,input().split()))
div = 2
divisor = 1
a = A
b = B
while(1):
    if(a%div == 0 and b %div == 0):
          a /= div
          b /= div
          divisor *= div
    else:
        div+=1
    if a < div or b < div:
        multiple = int(divisor*a*b)
        break
print(divisor)
print(multiple)