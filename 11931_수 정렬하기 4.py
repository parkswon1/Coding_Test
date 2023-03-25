import sys
N = int(sys.stdin.readline())

Plus_Numbers = [0]*1000000
Zero = 1
Minus_Numbers = [0]*1000000

for n in range(N):
    Number = int(sys.stdin.readline())
    if Number < 0:
        Minus_Numbers[abs(Number)-1] = Number
    elif Number == 0:
        Zero = 0
    else:
        Plus_Numbers[Number-1] = Number
        
for n in range(-1,-1000001,-1):
    if Plus_Numbers[n] != 0:
        print(Plus_Numbers[n])

if Zero == 0:
    print(0)

for n in range(1000000):
    if Minus_Numbers[n] != 0:
        print(Minus_Numbers[n])