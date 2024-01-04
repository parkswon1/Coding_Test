import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
time = 90//5
dp1 = []
dp2 = []
for n in range(19):
    dp1.append([0]*19)
    dp2.append([0]*19)
dp1[0][0] = 1
dp2[0][0] = 1

for i in range(1,19):
    for j in range(i):
        dp1[i][j] += dp1[i-1][j] * ((100 - A)/100)
        dp1[i][j+1] += dp1[i-1][j] * ((100 - A)/100)

        dp2[i][j] += dp2[i - 1][j] * ((100 - B)/100)
        dp2[i][j + 1] += dp2[i - 1][j] * ((100 - B)/100)

output = 0
for i in (2,3,5,7,13,17):
    output += dp1[18][i-1] + dp2[18][i-1]
sum(dp1[18])
print(output)
