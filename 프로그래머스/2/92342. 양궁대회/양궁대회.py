def solution(n, info):
    answer = [-1]
    diff = 0
    nodes = [(0, n, [0] * 11)]

    while nodes:
        i, arrow, board = nodes.pop()

        if i == 10:
            board[-1] = arrow

            pichCount = 0
            rianCount = 0

            for j in range(len(info)):
                if info[j] == 0 and board[j] == 0:
                    continue

                if board[j] > info[j]:
                    rianCount += 10 - j
                else:
                    pichCount += 10 - j

            currentDiff = rianCount - pichCount

            if currentDiff > 0:
                if currentDiff > diff:
                    answer = board[:]
                    diff = currentDiff

                elif currentDiff == diff:
                    for k in range(10, -1, -1):
                        if board[k] > answer[k]:
                            answer = board[:]
                            break
                        elif board[k] < answer[k]:
                            break

            continue

        if info[i] < arrow:
            board[i] = info[i] + 1
            nodes.append((i + 1, arrow - info[i] - 1, board[:]))
            board[i] = 0

        nodes.append((i + 1, arrow, board[:]))

    return answer