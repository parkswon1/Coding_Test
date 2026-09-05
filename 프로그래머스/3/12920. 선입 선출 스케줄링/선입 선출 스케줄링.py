def solution(n, cores):
    answer = 0
    front = 1
    back = 50000 * 100000
    while front < back:
        middle = (front + back) // 2
        wCount = len(cores)
        for c in cores:
            wCount += middle // c

        if wCount >= n:
            back = middle
        else:
            front = middle + 1

    beforCount = len(cores)
    for c in cores:
        beforCount += (front - 1) // c

    remain = n - beforCount

    for i in range(len(cores)):
        if front % cores[i] == 0:
            remain -= 1

            if remain == 0:
                return i + 1
