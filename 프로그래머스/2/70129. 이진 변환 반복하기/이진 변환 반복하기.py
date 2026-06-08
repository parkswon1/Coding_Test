def solution(s):
    answer = [0,0]
    while s != '1':
        answer[0] += 1
        s, zero = removeZero(s)
        answer[1] += zero
        s = change(len(s))
        
    return answer

def removeZero(s):
    return '1' * s.count("1"), s.count("0")

def change(num):
    s = ''
    while num != 0:
        s += str(num % 2)
        num = num // 2
    
    return s
    