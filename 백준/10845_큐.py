import sys
N = int(sys.stdin.readline())
queue =[]
front = 0
end = -1
for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        end +=1
        queue.append(int(command[1]))
    elif command[0] == 'pop':
        if front > end:
            print(-1)
        else:
            print(queue[front])
            front +=1
    elif command[0] == 'size':
        print(end-front+1)
    elif command[0] == 'empty':
        if front > end:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if front > end:
            print(-1)
        else:
            print(queue[front])
    elif command[0] == 'back':
        if front > end:
            print(-1)
        else:
            print(queue[end])