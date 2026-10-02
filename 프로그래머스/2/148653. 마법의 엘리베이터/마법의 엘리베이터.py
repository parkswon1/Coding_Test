def solution(storey):
    answer = 0

    while storey > 0:
        digit = storey % 10
        nextDigit = (storey // 10) % 10

        if digit > 5:
            answer += 10 - digit
            storey = storey // 10 + 1

        elif digit == 5 and nextDigit >= 5:
            answer += 5
            storey = storey // 10 + 1

        else:
            answer += digit
            storey //= 10

    return answer