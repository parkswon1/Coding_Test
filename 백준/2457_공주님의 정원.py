def search(start,end):
    global count
    Maxalivetime = max(days[start:end+1])
    count += 1
    if Maxalivetime >= 335:
        print(count)
        return
    elif Maxalivetime <= end:
        print(0)
        return
    else:
        search(end,Maxalivetime)

import sys
N = int(sys.stdin.readline())

start = 60
days = [0]*366
for i in range(N):
    line = list(map(int,sys.stdin.readline().split()))
    startday = line[1]
    endday = line[3]
    if line[0] == 2:
        startday += 31
    elif line[0] == 3:
        startday += 59
    elif line[0] == 4:
        startday += 90
    elif line[0] == 5:
        startday += 120
    elif line[0] == 6:
        startday += 151
    elif line[0] == 7:
        startday += 181
    elif line[0] == 8:
        startday += 212
    elif line[0] == 9:
        startday += 243
    elif line[0] == 10:
        startday += 273
    elif line[0] == 11:
        startday += 304
    elif line[0] == 12:
        startday += 334
    if line[2] == 2:
        endday += 31
    elif line[2] == 3:
        endday += 59
    elif line[2] == 4:
        endday += 90
    elif line[2] == 5:
        endday += 120
    elif line[2] == 6:
        endday += 151
    elif line[2] == 7:
        endday += 181
    elif line[2] == 8:
        endday += 212
    elif line[2] == 9:
        endday += 243
    elif line[2] == 10:
        endday += 273
    elif line[2] == 11:
        endday += 304
    elif line[2] == 12:
        endday += 334
    days[startday]=max(endday,days[startday])
    
count = 0
search(0,start)