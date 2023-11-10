def cal(l):
    global count
    if l < K:
        for c in range(len(case)):
            if l + case[c] ==K:
                count += 1
            elif l + case[c] < K:
                case.append(l+case[c])
        case.append(l)
    elif l == K:
        count+= 1

T = int(input())

for t in range(1,T+1):
    case = []
    count = 0
    N, K = map(int,input().split())
    line = list(map(int,input().split()))
    for l in line:
        cal(l)
    
    print(f"#{t}", count)