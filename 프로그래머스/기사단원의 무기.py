def solution(number, limit, power):
    answer = 1
    for num in range(2,number + 1):
        count = 0
        for i in range(1,int(num**(1/2)+1)):
            if num % i == 0:
                count += 1
                if i ** 2 != num:
                    count += 1

        if count > limit:
            count = power

        answer += count

    return answer

number = 10
limit = 3
power = 2
print(solution(number, limit, power))

