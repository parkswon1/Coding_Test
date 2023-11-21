T = int(input())

for test_case in range(1,T+1):
    N= int(input())
    str = []
    for n in range(N):
        word, count = input().split()
        for c in range(int(count)):
            str.append(word)
    index = 0
    i = 10
    l = len(str)
    print(f'#{test_case}')
    while(1):
        print(''.join(str[index:i]))
        if i >= l:
            break
        index = i
        i += 10