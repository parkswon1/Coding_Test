N = int(input())

def dfs(numbers,count):
    if count == N:
        answer = 0
        for i in range(10):
            answer += numbers[i]
        print(answer%1000000000)
        return
    output = []
    output.append(numbers[1])
    for i in range(1,9):
        output.append(numbers[i-1]+numbers[i+1])
    output.append(numbers[8])
    dfs(output,count+1)

N1 =[0,1,1,1,1,1,1,1,1,1]
dfs(N1,1)