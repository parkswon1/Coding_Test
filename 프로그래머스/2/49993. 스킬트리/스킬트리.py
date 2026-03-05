def solution(skill, skill_trees):
    answer = 0
    skillSet = set(list(skill))
    for tree in skill_trees:
        skillIndex = 0
        answer += 1
        for t in tree:
            if t in skillSet:
                if t == skill[skillIndex]:
                    skillIndex += 1
                else:
                    answer -= 1
                    break
            
            if skillIndex == len(skill):
                break
    
    return answer