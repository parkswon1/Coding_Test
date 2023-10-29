def DFS(index):
    global Start
    global Member_Count
    global Output
    if Student[index] == 0:
        return
    elif Student[index] == Start:
        Student[index] = 0
        Output += (Member_Count + 1)
        return
    else:
        Next_index = Student[index]
        Student[index] = 0
        Member_Count += 1
        DFS(Next_index-1)

T = int(input())

for t in range(T):
    n = int(input())
    Student = list(map(int,input().split()))
    Output = 0
    for st in range(n):
        Start = st + 1
        Member_Count = 0
        DFS(st)
    print(n - Output)