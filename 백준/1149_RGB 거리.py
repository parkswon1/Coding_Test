import sys
N = int(sys.stdin.readline())

house = list(map(int,sys.stdin.readline().split()))
for i in range(N-1):
    price =list(map(int,input().split()))
    red = min(house[1],house[2]) + price[0]
    green = min(house[0],house[2]) + price[1]
    blue = min(house[0],house[1]) + price[2]
    house[0] = red
    house[1] = green
    house[2] = blue
    
print(min(house))