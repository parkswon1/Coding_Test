import sys
N = int(sys.stdin.readline())
queue =[0]*20002
front = 10001
end = 10002
for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push_back':
        queue[end]= int(command[1])
        end +=1
    elif command[0] == 'push_front':
        queue[front]= int(command[1])
        front -=1
    elif command[0] == 'pop_front':
        if end-front-1 == 0:
            print(-1)
        else:
            front +=1
            print(queue[front])
    elif command[0] == 'pop_back':
        if end-front-1 == 0:
            print(-1)
        else:
            end -=1
            print(queue[end])
    elif command[0] == 'size':
        print(end-front-1)
    elif command[0] == 'empty':
        if end-front-1 == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if end-front-1 == 0:
            print(-1)
        else:
            print(queue[front+1])
    elif command[0] == 'back':
        if end-front-1 == 0:
            print(-1)
        else:
            print(queue[end-1])