def solution(s, skip, index):
    s = list(s)
    for i in range(len(s)):
        count = 0
        while(count != index):
            if s[i] == 'z':
                s[i] = 'a'
            else:
                s[i] = chr(ord(s[i]) + 1)

            if s[i] not in skip:
                count += 1

    return ''.join(s)

s = 'aukks'
skip = 'wbqd'
index = 5
print(solution(s, skip, index))