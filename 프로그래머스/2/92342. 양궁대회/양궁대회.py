def solution(n, info):
    answer = [-1, []]
    nodes = [(n, [0] * 11, 0)]

    while nodes:
        arrowCount, board, stage = nodes.pop()

        if stage == 11:
            newBoard = board[:]
            newBoard[-1] += arrowCount

            pichScore = 0
            rianScore = 0

            for i in range(11):
                if newBoard[i] > info[i]:
                    rianScore += 10 - i
                elif info[i] > 0:
                    pichScore += 10 - i

            diff = rianScore - pichScore

            if diff > 0:
                if answer[0] < diff:
                    answer = [diff, newBoard]
                elif answer[0] == diff:
                    for i in range(10, -1, -1):
                        if newBoard[i] > answer[1][i]:
                            answer = [diff, newBoard]
                            break
                        elif newBoard[i] < answer[1][i]:
                            break
            continue

        if arrowCount > info[stage]:
            newBoard = board[:]
            newBoard[stage] = info[stage] + 1
            nodes.append((arrowCount - newBoard[stage], newBoard, stage + 1))

        nodes.append((arrowCount, board[:], stage + 1))

    if answer[0] == -1:
        return [-1]

    return answer[1]