import sys

def attack(a,h):
    global curH,maxH
    if h % Hatk != 0:
        damage = a * (h // Hatk)
    else:
        damage = a * (h // Hatk - 1)
    curH += damage
    maxH = max(maxH,curH)
    return

def heal(a,h):
    global curH, Hatk
    curH -= h
    curH = min(curH,maxH)
    if curH < 1:
        curH = 1
    Hatk += a
    return

N, Hatk = map(int,sys.stdin.readline().split())
curH = 1
maxH = 1
for n in range(N):
    t, a, h = map(int,sys.stdin.readline().split())
    if t == 1:
        attack(a,h)
    else:
        heal(a,h)
print(maxH)