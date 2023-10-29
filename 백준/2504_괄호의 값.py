Parentheses = input()

Open_Parentheses = []
Output = 0
Count = 0
check = 0

for p in Parentheses:
    if p == ')':
        if len(Open_Parentheses) > 0:
            if Open_Parentheses[-1] == '(':
                if Count == 0:
                    Count += 2
                else:
                    Count *= 2
            else:
                check = 1
                break
        else:
            check = 1
            break
        
    elif p == ']':
        if len(Open_Parentheses) > 0:
            if Open_Parentheses[-1] == '[':
                if Count == 0:
                    Count += 3
                else:
                    Count *= 3
            else:
                check = 1
                break
        else:
            check = 1
            break
        
    else:
        Open_Parentheses.append(p)
    if len(Open_Parentheses) == 0:
        Output += Count
        Count = 0
        
if check == 0:
    print(Output)
else:
    print(0)