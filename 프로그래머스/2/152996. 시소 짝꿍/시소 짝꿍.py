from collections import defaultdict

def solution(weights):
    answer = 0
    dic = defaultdict(int)

    for w in weights:
        dic[w] += 1

    for w in sorted(dic):  # 중복 계산 방지
        count = dic[w]

        # 같은 무게끼리 조합 (1:1)
        if count >= 2:
            answer += count * (count - 1) // 2

        # 다른 무게 조합 (2:3, 1:2, 3:4)
        for a, b in [(2, 3), (1, 2), (3, 4)]:
            target = w * b / a
            if target.is_integer():
                target = int(target)
                if target in dic and target != w:
                    answer += count * dic[target]

    return answer