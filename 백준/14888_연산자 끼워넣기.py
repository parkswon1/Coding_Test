def search(n,cals,count):
    global high, low
    if count == N:
        if n < low:
            low = n
        if n > high:
            high = n
        return

    if cals[0] != 0:
        cals[0] -= 1
        search(n + A[count], cals, count + 1)
        cals[0] += 1
    if cals[1] != 0:
        cals[1] -= 1
        search(n - A[count], cals, count + 1)
        cals[1] += 1
    if cals[2] != 0:
        cals[2] -= 1
        search(n * A[count], cals, count + 1)
        cals[2] += 1
    if cals[3] != 0:
        cals[3] -= 1
        number = int(n/A[count])
        search(number, cals, count + 1)
        cals[3] += 1

N = int(input())

A = list(map(int,input().split()))
cals = list(map(int,input().split()))
high = -float('inf')
low = float('inf')

search(A[0],cals,1)

print(high)
print(low)