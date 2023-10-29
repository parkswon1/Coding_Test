while(1):
    x, y, z = list(map(int,input().split()))
    check = 0
    if x == 0 and y == 0 and z == 0:
        break
    if x == y:
        check += 1
    if y == z:
        check += 1
    if x == z:
        check += 1
    Max = max(x,y,z)
    if Max >= (x+y+z)-Max:
        print("Invalid")
    elif check == 3:
        print("Equilateral")
    elif check == 1:
        print("Isosceles")
    else:
        print("Scalene")