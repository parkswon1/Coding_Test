def solution(brown, yellow):
    x = 0
    while(1):
        x += 1
        y = yellow//x
        if x >= y:
            if brown == 2*y + 2*x + 4:
                return [x + 2,y + 2]

brown = 24
yellow = 24
print(solution(brown,yellow))