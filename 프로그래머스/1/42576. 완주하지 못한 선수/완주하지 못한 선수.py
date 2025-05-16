def solution(participant, completion):
    dict = {}
    for com in completion:
        if com not in dict:
            dict.setdefault(com,1)
        else:
            dict[com] = dict[com] + 1
    
    for par in participant:
        if par in dict:
            count = dict[par]
            count -= 1
            if count == -1:
                return par
            dict[par] = count
        else:
            return par