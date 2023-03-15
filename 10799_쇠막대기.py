import sys
Stick = sys.stdin.readline().rstrip()

Stick_Count = 0
Output = 0
for s in range(len(Stick)):
    if Stick[s] == '(':
        if Stick[s+1] == ')':
            Output += Stick_Count
        else:
            Stick_Count += 1
    else:
        if Stick[s-1] != '(': 
            Output += 1
            Stick_Count -= 1

print(Output)