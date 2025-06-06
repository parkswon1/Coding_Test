def solution(info, n, m):
    answer = float('inf')
    stack = [(0, 0, -1)]
    visited = set()  # 중복 상태 방지용

    while stack:
        Ascore, Bscore, infoIndex = stack.pop()
        nextIndex = infoIndex + 1

        if nextIndex == len(info):
            answer = min(answer, Ascore)
            continue

        key = (Ascore, Bscore, nextIndex)
        if key in visited:
            continue
        visited.add(key)

        Atrace, Btrace = info[nextIndex]

        if Ascore + Atrace < n:
            stack.append((Ascore + Atrace, Bscore, nextIndex))
        if Bscore + Btrace < m:
            stack.append((Ascore, Bscore + Btrace, nextIndex))

    return -1 if answer == float('inf') else answer