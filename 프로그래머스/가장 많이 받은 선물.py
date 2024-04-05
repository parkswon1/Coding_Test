def solution(friends, gifts):
    change = []
    jisu = [0] * len(friends)

    for f in friends:
        change.append([0] * len(friends))

    for g in gifts:
        A, B = g.split()
        AIndex = friends.index(A)
        BIndex = friends.index(B)
        change[AIndex][BIndex] += 1
        jisu[AIndex] += 1
        jisu[BIndex] -= 1

    maxGift = 0

    for y in range(len(friends)):
        giftCount = 0
        for x in range(len(friends)):
            if change[y][x] > change[x][y] or (change[y][x] == change[x][y] and jisu[x] < jisu[y]):
                giftCount += 1
        maxGift = max(maxGift, giftCount)

    return maxGift




friends = ["joy", "brad", "alessandro", "conan", "david"]
gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
print(solution(friends,gifts))