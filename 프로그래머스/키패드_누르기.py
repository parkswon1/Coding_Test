def solution(numbers, hand):
    answer = ''
    leftHand = 10
    rightHand = 12
    for n in numbers:
        if n == 1 or n == 4 or n == 7:
            answer += "L"
            leftHand = n
        elif n == 3 or n == 6 or n == 9:
            answer += "R"
            rightHand = n
        else:
            if n == 0:
                n = 11

            leftDiff = abs(n - leftHand)//3 + abs(n - leftHand)%3
            rightDiff = abs(n - rightHand)//3 + abs(n - rightHand)%3

            if leftDiff > rightDiff:
                answer += "R"
                rightHand = n
            elif leftDiff == rightDiff:
                if hand == "right":
                    rightHand = n
                    answer += "R"
                else:
                    answer += "L"
                    leftHand = n
            else:
                answer += "L"
                leftHand = n
    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))