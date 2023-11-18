import sys
N, M = map(int,sys.stdin.readline().split())

output = 0
cards = list(map(int,sys.stdin.readline().split()))

for x in range(N):
    for y in range(x+1,N):
        for z in range(y+1,N):
            if M - (cards[x] + cards[y] + cards[z]) >= 0:
                output=max(cards[x] + cards[y] + cards[z],output)

print(output)
