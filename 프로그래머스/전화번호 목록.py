def solution(phone_book):
    phone_book.sort()
    now = '-1'
    for p in phone_book:
        if now == p[:len(now)]:
            return False
        else:
            now = p
    return True

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))

#다른 사람의 풀이
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

"""
내가한 풀이는 
1. phone_book을 정렬 -> 문자열이기 때문에 앞글자가 작을수록 앞으로 온다. 즉 ["119", "97674223", "1195524421"]
이런식으로 있을때 119, 1195524421, 97674223 이런식으로 정렬된다.
2. 현제 저장한 번호가 now에 들어가고 다음 번호랑 비교
3 - 1. 현재번호랑 다음 번호의 앞에서 현재번호 만큼이 같으면 False바로 return
3 - 2. 다를경우 이제 현재번호는 다른 번호의 앞에 절대로 올 수 없으니(정렬을 해놔서) 다음번호를 현재번호로 사용 그리고 2번으로 감

시간 복잡도는 len(phone_book) = n 
nlong(n) + n

다른 사람의 풀이는
1. hash_map에 모든 phoen_book의 값 넣고 있다는 뜻인 1로 만들기
2. phone_book에서 번호를 하나 꺼냄
3. 번호를 한글자씩 꺼내서 temp에 저장하고 set에 있는지 비교

모든 전화번호의 길이를 다 더한 값 = m
시간 복잡도는
n + n * m
우선 m의 값은 최소 m >= n 왜냐하면 각전화번호의 길이가 1이면 m = n이고 이상일 경우 무조건 더크기 때문
따라서 내 풀이를 따르는 방식이 좋을 것 같다.
dict를 만드는 만큼 공간 복잡도에서도 손해를 본다.
"""