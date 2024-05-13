def solution(routes):
    answer = 0
    routes.sort(key = lambda x:x[1])
    now = -300000
    for route in routes:
        if route[0] > now:
            answer += 1
            now = route[1]
    return answer

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))