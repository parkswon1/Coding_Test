N = int(input())

Numbers = list(map(int,input().split()))

v = int(input())

Output = 0

for n in Numbers:
    if n == v:
        Output += 1
        
print(Output)