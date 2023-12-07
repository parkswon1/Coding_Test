import sys

string = sys.stdin.readline().rstrip()
word = sys.stdin.readline().rstrip()

index = 0
count = 0
while(1):
    if string[index] == word[0]:
        if string[index:index + len(word)] == word:
            count += 1
            index += len(word) - 1
    index += 1
    if index > len(string) - len(word):
        break

print(count)