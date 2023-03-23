def Div(a, b):
    if b == 1:  
        return a % C
    else:
        Next_Div = Div(a, b // 2)
        if b % 2 == 0:
            return Next_Div * Next_Div % C  
        else:
            return Next_Div * Next_Div * a % C  
        
import sys
A, B, C = list(map(int, sys.stdin.readline().split()))

Output = Div(A, B)
print(Output)