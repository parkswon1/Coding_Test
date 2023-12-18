import sys

N, K = map(int,sys.stdin.readline().split())
product = list(map(int,sys.stdin.readline().split()))

plug = []
output = 0
for k in range(K):
    if product[k] not in plug:
        if len(plug) != N:
            plug.append(product[k])
        else:
            check = [float('inf')]*N
            for i in range(N):
                for j in range(k,K):
                    if product[j] == plug[i]:
                        check[i] = j
                        break

            maxIndex = 0
            maxCount = 0
            for n in range(N):
                if check[n] > maxCount:
                    maxIndex = n
                    maxCount = check[n]

            plug[maxIndex] = product[k]

            output += 1

print(output)