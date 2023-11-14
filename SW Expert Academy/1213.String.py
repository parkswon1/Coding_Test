for i in range(1,11):
    test_case = int(input())
    search_string = input()
    string = list(input())
    count = 0
    for s in  range(len(string)-len(search_string)+1):
        if string[s] == search_string[0]:
            flag = 0
            for j in range(1,len((search_string))):
                if search_string[j] != string[s+j]:
                    flag = 1
                    break
            if flag == 0:
                count += 1

    print(f'#{test_case}',count)