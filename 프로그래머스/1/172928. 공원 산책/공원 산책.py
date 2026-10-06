def solution(park, routes):
    answer = []
    Y = len(park)
    X = len(park[0])

    for i in range(Y):
        for j in range(X):
            if park[i][j] == 'S':
                y, x = i, j
                break

    odict = {}
    odict['E'] = (0, 1)
    odict['S'] = (1, 0)
    odict['W'] = (0, -1)
    odict['N'] = (-1, 0)
    
    for r in routes:
        order, strNum = r.split(" ")
        num = int(strNum)
        dy, dx = odict[order]
        my, mx = y, x
        flag = True
        for n in range(num):
            my += dy
            mx += dx
            if Y > my >= 0 and X > mx >= 0:
                if park[my][mx] != 'X':
                    continue
                else:
                    flag = False
                    break
            else:
                flag = False
                break
                
        if flag:
            y, x = my, mx
        
    return [y, x]