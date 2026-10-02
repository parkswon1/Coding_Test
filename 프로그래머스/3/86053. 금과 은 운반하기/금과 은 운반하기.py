def solution(a, b, g, s, w, t):
    front = 0
    back = 2000000000000000000000000  # 2 * 10^14

    while front < back:
        time = (front + back) // 2

        gold = 0
        silver = 0
        total = 0

        for i in range(len(g)):
            count = (time + t[i]) // (2 * t[i])
            canMove = w[i] * count

            gold += min(canMove, g[i])
            silver += min(canMove, s[i])
            total += min(canMove, g[i] + s[i])

        if gold >= a and silver >= b and total >= a + b:
            back = time
        else:
            front = time + 1

    return front