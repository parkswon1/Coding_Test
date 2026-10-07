def solution(name, yearning, photo):
    dict = {}
    answer = []
    for i in range(len(name)):
        dict[name[i]] = yearning[i]
    
    for P in photo:
        temp = 0
        for p in P:
            if p not in dict:
                continue
            temp += dict[p]
        answer.append(temp)
    
    return answer