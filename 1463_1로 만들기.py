import sys
sys.setrecursionlimit(10**6)

def calculation(number,count):
    global Min
    if number == 1:
        Min = count
        return
    count += 1
    if count >= Min:
        return
    if number%3 == 0 and number >= 3:
        calculation(number//3,count)
    if number%2 == 0 and number >= 2:
        calculation(number//2,count)
    calculation(number-1,count)

N = int(input())
Min = 1000001
calculation(N,0)

print(Min)
