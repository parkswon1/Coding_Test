def solution(clothes):
    answer = 1
    dict = {}
    for c in clothes:
        if c[1] not in dict:
            dict[c[1]] = 1
        else:
            dict[c[1]] += 1

    for d in dict.values():
        answer *= d + 1

    return answer - 1

clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))