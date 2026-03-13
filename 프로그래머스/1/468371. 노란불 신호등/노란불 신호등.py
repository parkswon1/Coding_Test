import math

def getLcm(arr):
    lcm = arr[0]
    for i in range(1, len(arr)):
        lcm = (lcm * arr[i]) // math.gcd(lcm, arr[i])
    return lcm

def solution(signals):
    cycles = [sum(sig) for sig in signals]
    N = getLcm(cycles)
    
    for n in range(1, N + 1):
        allMatch = True
        for i in range(len(signals)):
            cycle = cycles[i]
            start = signals[i][0]
            end = signals[i][0] + signals[i][1]
            modVal = n % cycle
            
            if not (start < modVal <= end):
                allMatch = False
                break
                
        if allMatch:
            return n
            
    return -1