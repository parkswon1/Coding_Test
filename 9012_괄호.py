import sys
N = int(sys.stdin.readline())
for i in range(N):
    PS = sys.stdin.readline().strip()
    left = 0
    check = 0
    for j in PS:
        if j == '(':
            left += 1
        else:
            left -= 1
        if left < 0:
            break
    if left == 0:
        print("YES")
    else:
        print("NO")
    