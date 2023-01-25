import sys
N = int(sys.stdin.readline())

score = []
for i in range(N-1):
    score.append(int(sys.stdin.readline()))
    
Maxscore = int(input())

count = 0
for i in range(-1,-(N),-1):
    if score[i] >= Maxscore:
        count += score[i] - Maxscore + 1
        score[i] -= score[i] - Maxscore + 1
    Maxscore = score[i]

print(count)