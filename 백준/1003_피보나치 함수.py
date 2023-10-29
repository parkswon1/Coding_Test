import sys
N = int(sys.stdin.readline())

zero = [0]*41
one = [0]*41

zero[0] = 1
one[1] = 1

for i in range(2,41):
    zero[i] = zero[i-1]+zero[i-2]
    one[i] = one[i-1]+one[i-2]

for i in range(N):
    case = int(sys.stdin.readline())
    print(zero[case],one[case])