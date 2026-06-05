import heapq
from collections import deque

#bfs로 돌면서
#heapq에 사다리를 슬수있는곳을 남기기 높이, 좌표 식으로해서 낮은 높이로 정렳면서가기
#bfs로 사다리 없이 갈수있는곳 다 찾았다면 heapq에서 다음 좌표 꺼내기 이때 방문을 했다면 무시하기
#1,1에서 시작하고 bfs는 height보다 작은 칸만 움직이기 
def solution(land, height):
    answer = 0
    nextNodes = []
    heapq.heappush(nextNodes,(0,(0,0)))
    move = [(0,1),(0,-1),(1,0),(-1,0)]
    visited = set()
    
    while nextNodes:
        nodes = deque([])
        while nextNodes:
            cost, node = heapq.heappop(nextNodes)
            if node in visited:
                continue
            else:
                nodes.append(node)
                visited.add(node)
                answer += cost
                break
        
        while nodes:
            y,x = nodes.popleft()
            for dy, dx in move:
                my = y + dy
                mx = x + dx
                if 0 <= my < len(land) and 0 <= mx < len(land[0]):
                    if (my, mx) in visited:
                        continue
                    if abs(land[my][mx] - land[y][x]) > height:
                        heapq.heappush(nextNodes, (abs(land[my][mx] - land[y][x]), (my,mx)))
                        continue

                    visited.add((my, mx))
                    nodes.append((my, mx))
    
    return answer