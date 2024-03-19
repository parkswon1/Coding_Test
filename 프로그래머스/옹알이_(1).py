def solution(babbling):
    answer = 0
    for b in babbling:
        word = ""
        for w in b:
            word += w
            if word in say:
                word = ""
        if word == "":
            answer += 1
    return answer

say = ["aya", "ye", "woo", "ma"]
babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
print(solution(babbling))