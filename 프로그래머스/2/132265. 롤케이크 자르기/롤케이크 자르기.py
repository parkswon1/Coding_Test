def solution(topping):
    fdict = {}
    bdict = {}
    for t in topping:
        if t not in bdict:
            bdict[t] = 0
        bdict[t] += 1
    
    count = 0
    for t in topping:
        if t not in fdict:
            fdict[t] = 0
        fdict[t] += 1
        
        bdict[t] -= 1
        if bdict[t] == 0:
            bdict.pop(t)
        
        if len(fdict) == len(bdict):
            count += 1

    return count