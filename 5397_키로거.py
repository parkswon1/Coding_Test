import sys
Test_Case = int(sys.stdin.readline().rstrip())

for i in range(Test_Case):
    Password = sys.stdin.readline().rstrip()
    Front_Line = []
    Back_Line = []
    
    for p in Password:
        if p == '-':
            if len(Front_Line) != 0:    
                Front_Line.pop()
        elif p == '<':
            if len(Front_Line) != 0:
                Back_Line.append(Front_Line.pop())
        elif p == '>':
            if len(Back_Line) != 0:
                Front_Line.append(Back_Line.pop())
        else:
            Front_Line.append(p)
    
    for b in range(len(Back_Line)):
        Front_Line.append(Back_Line.pop())
        
    print(*Front_Line,sep='')