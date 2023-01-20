import sys
sys.setrecursionlimit(10**6)

def order(ciphers,count):
    global dp
    count += 1
    ciphers2 = [0]*10
    ciphers2[0] = dp
    for i in range(1,10):
        ciphers2[i] = ciphers2[i-1]-ciphers[i-1] 
        dp += ciphers2[i]
    if count == N:
        print(dp%10007)
        return
    order(ciphers2,count)
        
N = int(input())

dp = 10
ciphers = [1]*10
if N == 1:
    print(dp)
else:    
    order(ciphers, 1)