import sys
N = int(sys.stdin.readline())
Plist = [0]*1000001
Mlist = [0]*1000001
zero = 0
for i in range(N):
    a = int(sys.stdin.readline())
    if a <0:
        Mlist[a] =a
    elif a == 0:
        zero = 1
    else:
        Plist[a] =a

for i in range(len(Mlist)):
    if Mlist[i] != 0:
        print(Mlist[i])
if zero ==1:
    print(0)
for i in range(len(Plist)):
    if Plist[i] != 0 :
        print(Plist[i])