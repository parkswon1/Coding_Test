from collections import deque

def solution(want, number, discount):
    answer = 0
    wantdict = {}
    buydict = {}
    
    for i in range(len(want)):
        wantdict[want[i]] = number[i]
    
    que = deque([])
    for d in discount:
        if d not in buydict:
            buydict[d] = 0
        buydict[d] += 1
        que.append(d)
        
        if len(que) > 10:
            n = que.popleft()
            buydict[n] -= 1
            if buydict[n] == 0:
                buydict.pop(n)
        
        flag = True
        for w in wantdict:
            if w in buydict and buydict[w] >= wantdict[w]:
                continue
                
            flag = False
        if flag:
            print(d)
            answer += 1
    
    return answer