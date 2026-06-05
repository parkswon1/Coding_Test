def solution(s):
    answer = []
    result = [
        list(map(int, item.split(",")))
        for item in s[2:-2].split("},{")
    ]
    result.sort(key=lambda x : len(x))
    visited = set()
    for r in result:
        for j in r:
            if j not in visited:
                answer.append(j)
                visited.add(j)
    return answer