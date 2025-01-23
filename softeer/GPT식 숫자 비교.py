import sys

N = int(input().strip())
numbers = [input().strip() for _ in range(N)]

def gpt_sort_key(num):
    if '.' in num:
        x, y = num.split('.')
        return (int(x), int(y))
    else:
        return (int(num), -1)

numbers.sort(key=gpt_sort_key)

for num in numbers:
    print(num)