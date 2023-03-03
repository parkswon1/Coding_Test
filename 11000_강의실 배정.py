import sys
N = int(sys.stdin.readline())

time = []
for i in range(N):
    time.append(list(map(int,sys.stdin.readline().split())))

time.sort()

room = [time[0][1]]

for i in range(1,N):
    check = 0
    for j in range(len(room)):
        if time[i][0] >= room[j]:
            room[j] = time[i][1]
            check = 1
            break
    if check == 0:
        room.append(time[i][1])

print(len(room))