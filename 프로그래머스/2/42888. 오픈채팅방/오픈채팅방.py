def solution(records):
    answer = []
    idDict = {}
    result = ["","님이 들어왔습니다.", "님이 나갔습니다."]
    for record in records:
        info = record.split(" ")
        order = info[0]
        id = info[1]
        if order != 'Leave':
            name = info[2]
        
        if order == 'Enter':
            ordernum = 1
            idDict[id] = name
            answer.append(id + "|" + str(ordernum))
        elif order == 'Leave':
            ordernum = 2
            answer.append(id + "|" + str(ordernum))
        elif order == 'Change':
            idDict[id] = name
    
    for i in range(len(answer)):
        id, order = answer[i].split("|")
        answer[i] = idDict[id] + result[int(order)]
        
    return answer