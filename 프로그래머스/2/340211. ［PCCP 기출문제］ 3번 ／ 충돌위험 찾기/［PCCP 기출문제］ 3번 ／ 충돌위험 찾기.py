def solution(points, routes):
    answer = 0
    
    #튜플이 들어가고 x,y, goal 번호임
    #x = robots[i][0]
    #y = robots[i][0]
    #goal = robots[i][0]
    robots = []
    goalCount = len(routes[0])
    #라우트에서 로봇 좌표계산해 넣기
    for route in routes:
        x = points[route[0] - 1][0]
        y = points[route[0] - 1][1]
        robots.append((x, y, 1))
    
    stop = False
    while not stop:
        stop = True
        
        #중복수 계산
        answer += isDanger(robots)
        
        #로봇 이동
        for i in range(len(robots)):
            x1, y1, goal = robots[i]
            
            if goal < goalCount:
                x2 = points[routes[i][goal] - 1][0]
                y2 = points[routes[i][goal] - 1][1]

                mx, my = moveToGoal(x1, y1, x2, y2)
                stop = False

                #움직였는데 좌표가 목표지점이라면
                if (mx, my) == (x2, y2):
                    goal += 1

                robots[i] = (mx, my, goal)
            else:
                robots[i] = (-1, -1, 9999)
            
    
    return answer

def isDanger(robots):
    count = 0
    d = {}
    for robot in robots:
        if robot != (-1, -1, 9999):
            x = robot[0]
            y = robot[1]
            key = (x, y)

            if key in d:
                if d[key] == 0:
                    count += 1
                    d[key] = 1
            else:
                d[key] = 0

    return count


#x1,y1은 로봇위치 x2,y2는 도착지 위치
def moveToGoal(x1,y1, x2,y2):
    if x1 != x2:
        if x1 > x2:
            x1 -= 1
        else:
            x1 += 1
    
    elif y1 != y2:
        if y1 > y2:
            y1 -= 1
        else:
            y1 += 1
    
    return (x1,y1)