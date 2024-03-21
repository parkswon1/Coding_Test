def solution(numbers):
    global visited, set
    set = set()
    visited = [0] * len(numbers)
    recursive("",numbers)
    answer = len(set)
    return answer

def recursive(nownum,numbers):
    global count, answer
    if nownum != "" and isPrime(int(nownum)):
        set.add(int(nownum))

    if len(nownum) != len(numbers):
        for n in range(len(numbers)):
            if visited[n] == 0:
                visited[n] = 1
                recursive(nownum + numbers[n],numbers)
                visited[n] = 0

def isPrime(nownum):
    if nownum < 2:
        return False
    else:
        for i in range(2, nownum):
            if nownum%i == 0:
                return False
        return True

numbers = "011"
print(solution(numbers))