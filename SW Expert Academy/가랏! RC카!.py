T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    V = 0
    distance = 0
    for i in range(N):
        a = input()
        if a != '0':
            command, acc = map(int, a.split())
            if command == 1:
                V = V + acc
                distance += V
            elif command == 2:
                V -= acc
                if V < 0:
                    V = 0
                distance += V
        else:
            distance += V
    
        print(distance)
        
    print(f'#{test_case} {distance}')
