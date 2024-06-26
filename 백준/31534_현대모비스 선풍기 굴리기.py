import sys
import math

a, b, h = map(int, sys.stdin.readline().split())

if a == b:
    print(-1)

elif a == 0:
    print((b**2 + h**2) * math.pi)

elif a < b:
    x = b*h / (b-a)
    S = (x**2 + b**2)
    s = ((x-h)**2 + a**2)
    print((S-s)*math.pi)

else:
    x = a*h / (a-b)
    S = (x**2 + a**2)
    s = ((x-h)**2 + b**2)
    print((S-s)*math.pi)