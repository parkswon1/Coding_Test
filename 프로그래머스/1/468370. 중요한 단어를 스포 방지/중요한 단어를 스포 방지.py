def solution(message, spoilerRanges):
    isSpoiled = [False] * len(message)
    for r in spoilerRanges:
        for i in range(r[0], r[1] + 1):
            isSpoiled[i] = True
            
    nonSpoilerSet = set()
    spoilerList = []
    idx = 0
    
    for w in message.split(' '):
        start = idx
        end = idx + len(w) - 1
        idx += len(w) + 1
        
        hasSpoiler = False
        for i in range(start, end + 1):
            if isSpoiled[i]:
                hasSpoiler = True
                break
                
        if hasSpoiler:
            spoilerList.append(w)
        else:
            nonSpoilerSet.add(w)
            
    importantCount = 0
    seen = set()
    
    for w in spoilerList:
        if w not in nonSpoilerSet and w not in seen:
            importantCount += 1
            seen.add(w)
            
    return importantCount