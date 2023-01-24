import sys
formula = sys.stdin.readline().rstrip()

sign = 0
number = 0
i = 0
while(1):
    if i >= len(formula):
        break
    if formula[i] == '-':
        sign = 1
        i += 1
    elif formula[i] == '+':
        i += 1
    else:
        j = i
        while(1):
            i += 1
            if i >= len(formula):
                break
            elif formula[i] == '-' or formula[i] == '+':
                break
        if sign == 0:
            number += int(formula[j:i])
        else:
            number -= int(formula[j:i])
            
print(number)