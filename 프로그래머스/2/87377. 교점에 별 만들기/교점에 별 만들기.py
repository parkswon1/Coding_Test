def solution(lines):
    dot = []
    minX = float('inf')
    maxX = -float('inf')
    minY = float('inf')
    maxY = -float('inf')
    
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            A, B, E = lines[i]
            C, D, F = lines[j]
            
            det = A*D - B*C
            if det == 0: continue
            
            x = (B*F - E*D) / det
            y = (E*C - A*F) / det
            
            if x.is_integer() and y.is_integer():
                x, y = int(x), int(y)
                dot.append([x, y])
                minX = min(x, minX)
                maxX = max(x, maxX)
                minY = min(y, minY)
                maxY = max(y, maxY)

    width = maxX - minX + 1
    height = maxY - minY + 1
    grid = [['.' for _ in range(width)] for _ in range(height)]
    
    for x, y in dot:
        grid[maxY - y][x - minX] = '*'
    
    answer = ["".join(row) for row in grid]
    return answer