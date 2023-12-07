def min_removals_for_anagram(word1, word2):
    def count_characters(word):
        char_count = {}
        for char in word:
            char_count[char] = char_count.get(char, 0) + 1
        return char_count

    count1 = count_characters(word1)
    count2 = count_characters(word2)

    removals = 0
    for char, count in count1.items():
        removals += abs(count - count2.get(char, 0))

    for char, count in count2.items():
        if char not in count1:
            removals += count

    return removals

word1 = input().strip()
word2 = input().strip()

result = min_removals_for_anagram(word1, word2)

print(result)
