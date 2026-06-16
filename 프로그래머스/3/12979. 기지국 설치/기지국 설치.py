def solution(n, stations, w):
    answer = 0
    front = 0

    stations.append(n + w + 1)

    for i in range(len(stations)):
        s = stations[i]

        fL = (s - w - 1) - front

        if fL > 0:
            answer += (fL + (2 * w + 1) - 1) // (2 * w + 1)

        front = s + w

    return answer