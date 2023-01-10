import sys
A,B,V = list(map(int,sys.stdin.readline().split()))
daybefore = V-A
day = daybefore//(A-B)
remainder = daybefore%(A-B)
if remainder>0:
    day +=1 
print(day+1)