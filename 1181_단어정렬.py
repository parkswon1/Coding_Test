import sys
N = int(sys.stdin.readline())
char =[]
for i in range(N):
    char.append(sys.stdin.readline().rstrip())
setchar = set(char)
char=list(setchar)
char.sort()
char.sort(key = len)
for i in char:
    print(i)