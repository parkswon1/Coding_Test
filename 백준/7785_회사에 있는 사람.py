import sys
n = int(sys.stdin.readline())

dic = {}
for i in range(n):
    Input = list(sys.stdin.readline().split())
    if Input[1] == 'enter':
        dic[Input[0]] = 'enter'
    else:
        del dic[Input[0]]

Output = sorted(dic.keys(),reverse=True)
for o in Output:
    print(o)