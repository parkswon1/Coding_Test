import sys
sys.setrecursionlimit(10**7)

def search(string,n):
    if n > N:
        cal = 0
        flag = 1
        stack = ''
        for s in string:
            if s == '+':
                cal += flag * int(stack)
                stack = ''
                flag = 1
            elif s == '-':
                cal += flag * int(stack)
                stack = ''
                flag = -1
            elif s != ' ':
                stack = stack + s
        cal += flag * int(stack)
        if cal == 0:
            print(string)
        return

    for i in (' ','+','-'):
        search(string+i+f'{n}',n + 1)


T = int(input())
for t in range(T):
    N = int(input())
    string = '1'
    search(string,2)
    print()