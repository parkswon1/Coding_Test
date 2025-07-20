def solution(storey):
    answer = 0

    while storey > 0:
        digit = storey % 10
        next_digit = (storey // 10) % 10

        if digit > 5 or (digit == 5 and next_digit >= 5):
            answer += 10 - digit
            storey += 10 - digit  # 올림
        else:
            answer += digit       # 내림

        storey //= 10

    return answer