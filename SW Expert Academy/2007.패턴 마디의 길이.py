T = int(input())

for test_case in range(1,T+1):
    string = input()
    word = []
    for s in range(len(string)):
        word.append(string[s])
        check = 0
        for w in range(len(word)):
            if word[w] != string[s+w+1]:
                check = 1
                break
        if check == 0:
            break
    print(f'#{test_case}',len(word))