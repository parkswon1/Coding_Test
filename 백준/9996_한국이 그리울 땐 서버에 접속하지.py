import sys

N = int(sys.stdin.readline())
pattern = sys.stdin.readline().rstrip()
for i in range(len(pattern)):
    if pattern[i] == '*':
        front = pattern[:i]
        back = pattern[i+1:]
        break

for n in range(N):
    string = sys.stdin.readline().rstrip()
    if string[0:len(front)] == front and string[len(string) - len(back):] == back and len(string) >= len(pattern) - 1:
        print('DA')
    else:
        print('NE')