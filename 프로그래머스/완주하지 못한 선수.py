def solution(participant, completion):
    dict = {}
    for c in completion:
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1

    for p in participant:
        if p in dict:
            if dict[p] == 0:
                return p
            else:
                dict[p] -= 1
        else:
            return p

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))