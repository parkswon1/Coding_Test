def solution(phone_book):
    s = set(phone_book)
    
    for num in phone_book:
        for i in range(1, len(num)):
            if num[:i] in s:
                return False
    return True