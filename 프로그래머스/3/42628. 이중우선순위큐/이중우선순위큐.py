import heapq

def solution(operations):
    answer = []
    lowq = []
    highq = []
    delSet = set()
    
    for i in range(len(operations)):
        o = operations[i]
        oper, num = o.split()
        num = int(num)
        if oper =='I':
            heapq.heappush(lowq, (num, i))
            heapq.heappush(highq, (-num, i))
        if oper =='D' and num == 1:
            while highq:
                if highq[0][1] in delSet:
                    heapq.heappop(highq)
                else:
                    break
            if highq:
                number, id = heapq.heappop(highq)
                delSet.add(id)

        if oper =='D' and num == -1:
            while lowq:
                if lowq[0][1] in delSet:
                    heapq.heappop(lowq)
                else:
                    break
            if lowq:
                number, id = heapq.heappop(lowq)
                delSet.add(id)

    while lowq and lowq[0][1] in delSet:
        heapq.heappop(lowq)

    while highq and highq[0][1] in delSet:
        heapq.heappop(highq)
    
    if len(lowq) == 0:
        return [0,0]
    return [-highq[0][0], lowq[0][0]]