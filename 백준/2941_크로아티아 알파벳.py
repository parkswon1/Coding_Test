import sys
string = sys.stdin.readline().rstrip()

n = len(string)
index = 0
word = ['c=','c-','dz=','d-','lj','nj','s=','z=']
count = 0

while(1):
    check = 1
    for w in word:
        if w == string[index:index + len(w)]:
            check = len(w)

    index += check
    count += 1
    if index >= len(string):
        break

print(count)