def solution(sizes):
    big = []
    small = []
    for s in sizes:
        big.append(max(s))
        small.append(min(s))
    answer = max(big) * max(small)
    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))