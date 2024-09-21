def solution(m, n, startX, startY, balls):
    result = []
    
    for ball in balls:
        targetX, targetY = ball
        distances = []
        
        if not (startY == targetY and startX > targetX):
            distances.append((startX + targetX) ** 2 + (startY - targetY) ** 2)
        
        if not (startY == targetY and startX < targetX):
            distances.append((2 * m - startX - targetX) ** 2 + (startY - targetY) ** 2)
        
        if not (startX == targetX and startY > targetY):
            distances.append((startX - targetX) ** 2 + (startY + targetY) ** 2)
        
        if not (startX == targetX and startY < targetY):
            distances.append((startX - targetX) ** 2 + (2 * n - startY - targetY) ** 2)
        
        result.append(min(distances))
    
    return result