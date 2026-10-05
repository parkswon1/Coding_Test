def solution(players, callings):
    answer = []
    dict = {}
    for i in range(len(players)):
        dict[players[i]] = i
    
    for c in callings:
        i = dict[c]
        temp = players[i - 1]
        players[i - 1] = c
        players[i] = temp
        
        dict[c] = i - 1
        dict[temp] = i
        
    return players