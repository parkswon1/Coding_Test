import sys

for t in range(int(sys.stdin.readline())):
    index = [[] for _ in range(26)]
    str = list(sys.stdin.readline().rstrip())
    K = int(sys.stdin.readline())
    low = [float('inf'),-1,-1,-1]
    for i in range(len(str)):
        nowNum = ord(str[i]) - 97
        index[nowNum].append(i)
        if len(index[nowNum]) >= K:
            low = min(low,[index[nowNum][-1] - index[nowNum][-K], index[nowNum][-K], index[nowNum][-1],nowNum])


    index2 = [-1] * 26
    first, end, num = low[1], low[2], low[3]
    for i in range(first):
        nowNum = ord(str[i]) - 97
        if num == nowNum:
            break
        if index2[nowNum] == -1:
            index2[nowNum] = i

    flag = 0
    output = -1
    for j in range(end + 1,len(str)):
        nowNum = ord(str[j]) - 97
        if num == nowNum:
            break
        if index2[nowNum] != -1:
            output = max(output ,j - index2[nowNum] + 1)
            flag = 1
            break
    if flag == 0:
        print(-1)
    else:
        print(low[2] - low[1] + 1,output)
