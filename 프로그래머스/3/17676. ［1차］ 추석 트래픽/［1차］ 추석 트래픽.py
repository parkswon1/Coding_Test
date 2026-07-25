def solution(lines):
    answer = 0
    parsedLines = []

    for line in lines:
        parts = line.split(" ")
        
        timeStr = parts[1]
        hour = int(timeStr[:2]) * 3600 * 1000
        minute = int(timeStr[3:5]) * 60 * 1000
        second = int(timeStr[6:8]) * 1000
        milliSecond = int(timeStr[9:12])
        
        endTime = hour + minute + second + milliSecond
        processingTime = int(round(float(parts[2][:-1]) * 1000))
        startTime = endTime - processingTime + 1
        
        parsedLines.append((startTime, endTime))
    
    for i in range(len(parsedLines)):
        for checkTime in [parsedLines[i][0], parsedLines[i][1]]:
            checkEnd = checkTime + 999
            count = 0
            
            for start, end in parsedLines:
                if start <= checkEnd and end >= checkTime:
                    count += 1
            
            answer = max(answer, count)
            
    return answer