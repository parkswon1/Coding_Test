import sys

def search():
    global output
    j = N - 1
    for i in range(N):
        check = [float('inf'),0,0]
        while i != j:
            diff = abs(liquid[i] + liquid[j])
            if diff < check[0]:
                check = [diff,liquid[i],liquid[j]]
                j -= 1
            else:
                j += 1
                break

        if output[0] > check[0]:
            output[0] = check[0]
            output[1] = check[1]
            output[2] = check[2]

        if i == j:
            return

N = int(sys.stdin.readline())
liquid = list(map(int, sys.stdin.readline().split()))
output = [float('inf'),1,1]
search()

print(output[1],output[2])