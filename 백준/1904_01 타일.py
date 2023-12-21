N= int(input())

dp1 = 1
if N > 1:
    dp2 = 2
    for n in range(3,N+1):
        dpn = (dp1 + dp2)%15746
        dp1 = dp2
        dp2 = dpn
if N == 1:
    print(dp1)
elif N == 2:
    print(dp2)
else:
    print(dpn)