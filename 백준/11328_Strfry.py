def count_characters(string):

    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

N = int(input())
for n in range(N):
    a_string,b_string = input().split()

    a_char_count = count_characters(a_string)
    b_char_count = count_characters(b_string)


    # 특정 문자의 개수가 같은지 비교
    if a_char_count == b_char_count:
        print("Possible")
    else:
        print("Impossible")
