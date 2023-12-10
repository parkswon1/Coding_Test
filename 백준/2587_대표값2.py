odd =[]
for i in range(5):
    N = int(input())
    odd.append(N)

odd.sort()
print(int(sum(odd)/5))
print(odd[2])
