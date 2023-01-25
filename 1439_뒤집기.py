import sys
S = list(sys.stdin.readline().rstrip())

i = 0
sign = S[0]
onecount = 0
zerocount = 0
lenth = len(S)
while(1):
    if S[i] == sign:
        if sign == '0':
            zerocount += 1
            sign = '1'
        else:
            onecount += 1
            sign = '0'
    i += 1
    if lenth == i:
        break
print(min(onecount,zerocount))