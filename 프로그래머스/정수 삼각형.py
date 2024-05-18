def solution(triangle):
    answer = 0
    answerTriangle = []
    for i in range(1, len(triangle) + 1):
        answerTriangle.append([0] * i)

    answerTriangle[0][0] = triangle[0][0]

    for y in range(len(triangle) - 1):
        Y = y + 1
        for x in range(len(triangle[y])):
            for i in (0, 1):
                X = x + i
                answerTriangle[Y][X] = max(answerTriangle[Y][X], answerTriangle[y][x] + triangle[Y][X])

    return max(answerTriangle[-1])

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))