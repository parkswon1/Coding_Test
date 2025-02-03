def solution(N, results):
    answer = 0
    winners = [set() for _ in range(N)]
    losers = [set() for _ in range(N)]

    for winner, loser in results:
        winners[winner - 1].add(loser - 1)
        losers[loser - 1].add(winner - 1)

    for n in range(N):
        for winner in winners[n]:
            losers[winner] |= losers[n]
        for loser in losers[n]:
            winners[loser] |= winners[n]

    for n in range(N):
        if len(winners[n]) + len(losers[n]) == N - 1:
            answer += 1

    return answer