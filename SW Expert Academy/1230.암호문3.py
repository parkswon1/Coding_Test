for test_case in range(1, 11):
    input()	
    original = input().split()	
    input()
    cmd = input().split()
    for idx in range(len(cmd)):
        if cmd[idx] == 'A':		
            y = int(cmd[idx + 1])
            for i in range(y):
                original.append(cmd[idx + i + 2])
        elif cmd[idx] == 'I':
            x = int(cmd[idx + 1])
            y = int(cmd[idx + 2])
            for i in range(y):
                original.insert(x + i, cmd[idx + i + 3])
        elif cmd[idx] == 'D':
            x = int(cmd[idx + 1])
            y = int(cmd[idx + 2])
            for i in range(y):
                original.pop(x + i)
    print("#", test_case, sep="", end="")
    for i in range(10):
        print(" ", original[i], sep="", end="")
    print()