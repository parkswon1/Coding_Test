odd =[]
for i in range(7):
    N = int(input())
    if N % 2 != 0:
        odd.append(N)

odd.sort()
if len(odd) != 0:
    print(sum(odd))
    print(odd[0])
else:
    print(-1)