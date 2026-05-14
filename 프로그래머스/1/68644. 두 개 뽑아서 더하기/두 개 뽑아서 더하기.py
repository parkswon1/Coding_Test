def solution(numbers):
    answer = set()
    #반복문을 두번 돌려 모든 가짓수 만들기
    #set에다가 답을 담고 리거를 list로 만들고 return하기
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i] + numbers[j])
    answer = list(answer)
    answer.sort()
    return answer