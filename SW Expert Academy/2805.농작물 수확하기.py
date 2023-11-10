T = int(input())

for t in range(1,T+1):
    N = int(input())
    center = int(N/2 + 0.5)
    output = 0
    for i in range(center):
        line = [int(n) for n in str(input())]
        output += sum(line[center-i-1:center] + line[center:center + i])
    for i in  range(1,center):
        line = [int(n) for n in str(input())]
        output += sum(line[0+i:center] + line[center:N - i])
    print(f"#{t}",output)