from collections import deque

def solution(sequence, k):
    answer = []
    answerlen = float('inf')
    que = deque([])
    
    count = 0
    front = 0
    for i in range(len(sequence)):
        que.append(sequence[i])
        count += sequence[i]
        while count > k and que:
            count -= que.popleft()
            front += 1
        if count != k or len(que) >= answerlen:
            continue
        
        answerlen = len(que)
        answer = [front, i]
        
    return answer