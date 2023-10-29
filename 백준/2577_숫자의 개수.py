Count = [0]*10
A = int(input())
B = int(input())
C = int(input())
Temp = A*B*C
Numbers = str(Temp)
    
for n in Numbers:
    Count[int(n)] += 1
    
for c in Count:
    print(c)