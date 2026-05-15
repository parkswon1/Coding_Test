from collections import deque

rightSet = [['(',')'], ['[',']'], ['{','}']]

#검증하는 함수를 만들어서 검증하면 될듯
def isTrue(S):
    stack = []
    for s in S:
        stack.append(s)
        if len(stack) > 1:
            if [stack[-2],stack[-1]] in rightSet:
                stack.pop()
                stack.pop()
    
    if len(stack) > 0:
        return False
    return True
            

def solution(s):
    answer = 0
    #회전시키기 아마도 deque를 사용해서 list를 회전시키면 될듯
    s = deque(s)
    for i in range(len(s)):
        if isTrue(s):
            answer += 1
        s.append(s.popleft())
        
    #회전시키면서 검증하기
    return answer