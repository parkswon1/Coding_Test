def solution(participant, completion):
    answer = ''
    dict = {}
    for c in completion:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    
    for p in participant:
        if p not in dict:
            return p
        dict[p] -= 1
        if dict[p] == 0:
            dict.pop(p)
        
    return answer